from aiogram.types import Message

from loader import dp
from Keybords import create_keyboard


"""
Handler на 
* для параметров commands наименование команд указывается без '/'
"""
@dp.message_handler(content_types=["location"])
async def get_location(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.reply(f'Ну все, {name}. Теперь я знаю, где ты!', reply_markup=create_keyboard(name, user))