from aiogram import types
import random
from .keyboards.reply import get_during_game_menu
from .difficulties import get_description, get_attempts, get_range

current_attempt = 0
ATTEMPTS = 0
SECRET_NUMBER = 0

def game(number: int) -> str:
    global current_attempt
    current_attempt += 1

    if current_attempt > ATTEMPTS:
        return f"Количество попыток закончилось...\nЗагаданное число - {SECRET_NUMBER}"
    elif number == SECRET_NUMBER:
        return f"Вы выиграли! Загаданное число - {SECRET_NUMBER}"
    elif number < SECRET_NUMBER:
        return f"Загаданное число БОЛЬШЕ\nПопыток осталось: {ATTEMPTS - current_attempt}"
    elif number > SECRET_NUMBER:
        return f"Загаданное число МЕНЬШЕ\nПопыток осталось: {ATTEMPTS - current_attempt}"
    
    return 'Другое'

async def start_game(message: types.Message, difficulty: str):
    global current_attempt
    global ATTEMPTS
    global SECRET_NUMBER

    current_attempt = 0
    ATTEMPTS = get_attempts(difficulty)
    RANGE = get_range(difficulty)
    SECRET_NUMBER = random.randint(1, RANGE)

    await message.answer(f"Сложность: {get_description(difficulty)}\n"
                         f"Попыток: {ATTEMPTS}\n"
                         f"Диапазон: {RANGE}",
                         reply_markup=get_during_game_menu())
    
    await message.answer('Введите число')
    