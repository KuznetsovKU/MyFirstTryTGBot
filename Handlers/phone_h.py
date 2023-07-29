from aiogram.types import Message

from loader import dp
from Keybords import create_keyboard


"""
Handler на 
* для параметров commands наименование команд указывается без '/'
"""
@dp.message_handler(content_types=["contact"])
async def get_phone(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.reply(f'{name}, спасибо! Твой контакт получен!', reply_markup=create_keyboard(name, user))