import datetime
from typing import Any

from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Next, Button, Back
from aiogram_dialog.widgets.text import Format, Jinja, Const
from aiogram_dialog.widgets.input import TextInput

from services.backend import BackendClient

router = Router()


class TaskCreationStates(StatesGroup):
    content = State()
    category = State()
    due_time = State()
    result = State()


async def error(
    message: Message, dialog_: Any, manager: DialogManager, error_: ValueError
):
    await message.answer("Age must be a number!")


def get_time(str_date: str) -> str:
    return str(datetime.datetime.strptime(str_date, "%d.%m.%Y").date())


async def send_task_data(
    callback: CallbackQuery, button: Button, manager: DialogManager
):
    await BackendClient.add_task(
        content=manager.find("content").get_value(),
        category=manager.find("category").get_value(),
        due_time=manager.find("due_time").get_value(),
        user_tg_id=callback.from_user.id,
    )

    await manager.done()


async def get_form(dialog_manager: DialogManager, **kwargs):
    return {
        "content": dialog_manager.find("content").get_value(),
        "category": dialog_manager.find("category").get_value(),
        "due_time": dialog_manager.find("due_time").get_value(),
    }


@router.callback_query(F.data == "task_add")
async def add_task(callback: CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(TaskCreationStates.content, mode=StartMode.RESET_STACK)


dialog = Dialog(
    Window(
        Format("Введите задачу"),
        TextInput(id="content", on_success=Next()),
        state=TaskCreationStates.content,
    ),
    Window(
        Format("Введите категорию"),
        TextInput(id="category", on_success=Next()),
        state=TaskCreationStates.category,
    ),
    Window(
        Format("Введите время в формате D.M.Y"),
        TextInput("due_time", on_success=Next(), on_error=error, type_factory=get_time),
        state=TaskCreationStates.due_time,
    ),
    Window(
        Jinja(
            "<b>You entered</b>:\n\n"
            "<b>content</b>: {{content}}\n"
            "<b>category</b>: {{category}}\n"
            "<b>due_time</b>: {{due_time}}\n"
        ),
        Button(Const("Подтвердить"), id="confirm", on_click=send_task_data),
        Back(Const("Назад")),
        getter=get_form,
        state=TaskCreationStates.result,
        parse_mode="html",
    ),
)
