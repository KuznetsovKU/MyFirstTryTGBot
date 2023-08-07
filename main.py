from aiogram.utils import executor

from Handlers import dp
from Database import create_users_table


async def on_start(_):
    print('Database running... ', end='')
    try:
        create_users_table()
        print("Succesfuly")
    except:
        print("FAILURE")
    print("Бот запущен")
    print("first change to commit")
    print("second change to commit")
    print("third change to commit")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)