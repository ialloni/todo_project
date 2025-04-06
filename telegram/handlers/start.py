from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from keyboards.start_keyboard import get_keyboard
from phrases import CMD_START

router = Router()


@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(
        text=CMD_START,
        reply_markup=get_keyboard(),
        parse_mode=ParseMode.HTML,

    )
