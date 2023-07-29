from aiogram.types import Message

from loader import dp
from Keybords import create_keyboard


"""
Handler на сбор остальных запросов
* для параметров commands наименование команд указывается без '/'
"""
@dp.message_handler()  # Handler без параметров ловит все подряд
async def empty_request(message: Message):
    name = message.from_user.first_name
    user = message.from_user.id
    print(message)
    await message.answer(f"{message.from_user.first_name}, мая твая нипанимай! \n Что за '{message.text}'? \n "
                         f"Давай, лучше по кнопочкам потыкай ;))", reply_markup=create_keyboard(name, user))

