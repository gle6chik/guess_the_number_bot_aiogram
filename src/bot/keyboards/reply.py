from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def get_persistent_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Правила игры')],
            [KeyboardButton(text='Ещё что-нибудь')],
            [KeyboardButton(text='Ну еще что-то')]
        ],
        resize_keyboard=True, # Подстраивание размера кнопки
        is_persistent=True, # Создание кнопки открытия/закрытия меню рядом с полем ввода
    )

def get_remove_menu():
    return ReplyKeyboardRemove()
