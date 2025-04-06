from aiogram import Router, types, F
from services.backend import BackendClient

router = Router()


@router.callback_query(F.data == "task_list")
async def list_tasks(callback: types.CallbackQuery):
    tasks = await BackendClient.get_tasks({"user_tg_id": callback.from_user.id})
    try:
        await callback.message.answer(text=f"{BackendClient.parse_tasks(tasks)}")
    except:
        await callback.message.answer(text="У вас нет запланированных задач")
