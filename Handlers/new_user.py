from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from loader import dp
from Keybords import create_keyboard


@dp.message_handler(commands=['start'])
async def new_user(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.answer(f'{message.from_user.first_name}, привет!', reply_markup=create_keyboard(name, user))