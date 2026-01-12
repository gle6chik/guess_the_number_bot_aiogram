from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=f"Новая игра")],
            [KeyboardButton(text=f"Правила игры")],
            [KeyboardButton(text=f"О боте")]
        ],
        resize_keyboard=True, # Подстраивание размера кнопки
        is_persistent=True, # Создание кнопки открытия/закрытия меню рядом с полем ввода
    )