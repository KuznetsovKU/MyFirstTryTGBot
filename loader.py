import os
from aiogram import Bot, Dispatcher

my_source = '@MyFirstTry1Bot'

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)