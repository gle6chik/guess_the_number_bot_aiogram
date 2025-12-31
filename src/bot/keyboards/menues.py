from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Новая игра')],
            [KeyboardButton(text='Правила игры')],
            [KeyboardButton(text='О боте')]
        ],
        resize_keyboard=True, # Подстраивание размера кнопки
        is_persistent=True # Создание кнопки открытия/закрытия меню рядом с полем ввода
    )

def get_second_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Test1')],
            [KeyboardButton(text='Test2')],
            [KeyboardButton(text='Test3')]
        ],
        resize_keyboard=True,
        is_persistent=True
    )
