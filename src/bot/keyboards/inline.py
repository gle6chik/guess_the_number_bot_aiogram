from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_choice_of_difficulty():
    builder = InlineKeyboardBuilder()
    
    builder.button(text='Лёгкий', callback_data='start_easy')
    builder.button(text='Средний', callback_data='start_medium')
    builder.button(text='Сложный', callback_data='start_difficult')
    builder.button(text='Назад', callback_data='back')

    builder.adjust(1) # Расположение кнопок по вертикали в 1 столбец

    return builder.as_markup()