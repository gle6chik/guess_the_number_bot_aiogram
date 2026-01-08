from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_during_game_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Выйти из игры')]
        ],
        resize_keyboard=True,
        is_persistent=True
    )