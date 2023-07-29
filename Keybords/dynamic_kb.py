from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

switch = '/start'
clicks = {}

def create_keyboard(name: str, user_id: int) -> ReplyKeyboardMarkup:
    global switch
    global clicks
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if switch == '/start':
        switch = '/help'
    else:
        switch = '/start'

    clicks[user_id] = clicks.get(user_id, 0)

    btn_start = KeyboardButton(text='/start')
    btn_help = KeyboardButton(text='/help')
    btn_name = KeyboardButton(text=name)
    btn_switch = KeyboardButton(text=switch)
    btn_counter = KeyboardButton(text=clicks[user_id])
    btn_counter_reset = KeyboardButton(text='/reset_clicks')
    btn_location = KeyboardButton(text='GEO', request_location=True)
    btn_phone = KeyboardButton(text='PHONE', request_contact=True)

    keyboard.row(btn_start, btn_switch, btn_help)
    keyboard.row(btn_name)
    keyboard.row(btn_counter, btn_counter_reset)
    keyboard.row(btn_location, btn_phone)
    return keyboard


def create_kb_with_click_count(name: str, user_id: int) -> ReplyKeyboardMarkup:
    global switch
    global clicks
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if switch == '/start':
        switch = '/help'
    else:
        switch = '/start'

    clicks[user_id] = clicks.get(user_id, 1) + 1

    btn_start = KeyboardButton(text='/start')
    btn_help = KeyboardButton(text='/help')
    btn_name = KeyboardButton(text=name)
    btn_switch = KeyboardButton(text=switch)
    btn_counter = KeyboardButton(text=clicks[user_id])
    btn_counter_reset = KeyboardButton(text='/reset_clicks')
    btn_location = KeyboardButton(text='GEO', request_location=True)
    btn_phone = KeyboardButton(text='PHONE', request_contact=True)

    keyboard.row(btn_start, btn_switch, btn_help)
    keyboard.row(btn_name)
    keyboard.row(btn_counter, btn_counter_reset)
    keyboard.row(btn_location, btn_phone)
    return keyboard


def create_kb_reseted_clicks(name: str, user_id: int) -> ReplyKeyboardMarkup:
    global switch
    global clicks
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if switch == '/start':
        switch = '/help'
    else:
        switch = '/start'
    clicks[user_id] = 0

    btn_start = KeyboardButton(text='/start')
    btn_help = KeyboardButton(text='/help')
    btn_name = KeyboardButton(text=name)
    btn_switch = KeyboardButton(text=switch)
    btn_counter = KeyboardButton(text=clicks[user_id])
    btn_counter_reset = KeyboardButton(text='/reset_clicks')
    btn_location = KeyboardButton(text='GEO', request_location=True)
    btn_phone = KeyboardButton(text='PHONE', request_contact=True)

    keyboard.row(btn_start, btn_switch, btn_help)
    keyboard.row(btn_name)
    keyboard.row(btn_counter, btn_counter_reset)
    keyboard.row(btn_location, btn_phone)
    return keyboard