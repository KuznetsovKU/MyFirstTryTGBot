from aiogram.types import Message

from loader import dp
from Keybords import create_keyboard


"""
Handler на команду /Start
* для параметров commands наименование команд указывается без '/'
"""
@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.answer(f'{message.from_user.first_name}, привет!', reply_markup=create_keyboard(name, user))

