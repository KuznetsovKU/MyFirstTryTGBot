from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as InlineKB
from .callbacks import inline_keyboard


def create_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=3)
    button_1 = InlineKB(text='Нажми меня', callback_data=inline_keyboard.new(menu='main', button='first'))
    keyboard.add(button_1)
    return keyboard
