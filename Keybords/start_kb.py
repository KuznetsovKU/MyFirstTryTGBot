from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_start = KeyboardButton(text='/start')
btn_location = KeyboardButton(text='GEO', request_location=True)
btn_phone = KeyboardButton(text='PHONE', request_contact=True)
keyboard.add(btn_start,  btn_location, btn_phone)

