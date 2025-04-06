from datetime import timedelta

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession

from celery import Celery

import asyncio

from config_reader import config
from services.backend import BackendClient

app_celery = Celery("bot_celery", broker=config.ADDRESS_REDIS)

app_celery.conf.beat_schedule = {
    "send_message-every-day": {
        "task": "send_task_notify",
        "schedule": timedelta(days=1),
    }
}


@app_celery.task(name="send_task_notify")
def send_notify():
    asyncio.run(send_notify_async())


async def send_notify_async():
    bot = Bot(token=config.bot_token.get_secret_value(), session=AiohttpSession())
    try:
        tasks = await BackendClient.get_today_tasks()
        for task in tasks:
            tg_user_id = task.get("user_tg_id")
            message = f"Напоминание: {task.get('content')}  +   {task.get('category')}"
            if tg_user_id:
                try:
                    await bot.send_message(tg_user_id, message)
                except:
                    pass
    finally:
        await bot.session.close()
