from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard():
    button = InlineKeyboardButton(text='Task List', callback_data='task_list')
    button2 = InlineKeyboardButton(text='Add Task', callback_data='task_add')

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button, button2]], resize_keyboard=True)
    return keyboard