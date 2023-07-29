from aiogram.types import Message

from loader import dp
from Keybords import create_kb_with_click_count, create_keyboard, create_kb_reseted_clicks

"""
Handler на команду /Start
* для параметров commands наименование команд указывается без '/'
"""
@dp.message_handler(lambda message: message.text.isdigit())
async def count_clicks(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.answer(f'+ 1', reply_markup=create_kb_with_click_count(name, user))


@dp.message_handler(commands=['reset_clicks'])
async def reset_clicks_counter(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.reply(f'Счетчик сброшен', reply_markup=create_kb_reseted_clicks(name, user))