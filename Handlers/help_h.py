from aiogram.types import Message

from loader import dp
from Keybords import keyboard, create_keyboard


"""
Handler на команду /help
* для параметров commands наименование команд указывается без '/'
"""
@dp.message_handler(commands=['help'])
async def help_request(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.answer(f'Пааа-мааа-гиии-теее!!!', reply_markup=create_keyboard(name, user))