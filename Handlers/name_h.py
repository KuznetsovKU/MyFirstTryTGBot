from aiogram.types import Message

from loader import dp
from Keybords import create_keyboard

"""
Handler на команду /Start
* для параметров commands наименование команд указывается без '/'
"""


@dp.message_handler(lambda message: message.text == message.from_user.first_name)
async def count_clicks(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.answer(f"Да, это ты. Тебя действительно зовут {name}", reply_markup=create_keyboard(name, user))