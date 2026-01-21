from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_choice_of_difficulty():
    builder = InlineKeyboardBuilder()
    
    builder.button(text='Лёгкий', callback_data='start_easy')
    builder.button(text='Средний', callback_data='start_medium')
    builder.button(text='Сложный', callback_data='start_hard')
    builder.button(text='Назад', callback_data='back')

    builder.adjust(2, 2) # Расположение кнопок в таблице 2 на 2

    return builder.as_markup()

def get_cleaning_of_statistics():
    builder = InlineKeyboardBuilder()
    builder.button(text='Сбросить статистику', callback_data='clean_statistics')
    return builder.as_markup()

def get_rating_information():
    builder = InlineKeyboardBuilder()
    builder.button(text='Справка', callback_data='about_rating')
    return builder.as_markup()
