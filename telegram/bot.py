import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config
import logging
from aiogram_dialog import setup_dialogs


logging.basicConfig(level=logging.INFO)

from handlers import start, list_tasks, add_task


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(list_tasks.router)
    dp.include_router(add_task.router)
    dp.include_router(add_task.dialog)

    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
