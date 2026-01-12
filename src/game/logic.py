from aiogram import types
import random
from .keyboards.reply import get_during_game_menu
from .difficulties import get_description, get_attempts, get_range

user_games = {}

def game(user_id: int, number: int):
    game_data = user_games[user_id]
    game_data['current_attempt'] += 1

    if number == game_data['secret_number']:
        secret_num = game_data['secret_number']
        del user_games[user_id]
        return f"Победа! На {game_data['current_attempt']} попытке из {game_data['attempts']}! Ты молодец! Загаданное число - {secret_num}", 1

    if game_data['current_attempt'] >= game_data['attempts']:
        secret_num = game_data['secret_number']
        del user_games[user_id]
        return f"Количество попыток закончилось...\nЗагаданное число - {secret_num}\nНе переживай, в следующий раз повезёт!", 1
    
    elif number < game_data['secret_number']:
        attempts_left = game_data['attempts'] - game_data['current_attempt']
        return f"Загаданное число БОЛЬШЕ {number}\nПопыток осталось: {attempts_left}", 0
    elif number > game_data['secret_number']:
        attempts_left = game_data['attempts'] - game_data['current_attempt']
        return f"Загаданное число МЕНЬШЕ {number}\nПопыток осталось: {attempts_left}", 0

async def start_game(message: types.Message, difficulty: str, user_id: int):
    attempts = get_attempts(difficulty=difficulty)
    range_num = get_range(difficulty=difficulty)
    secret_number = random.randint(1, range_num)

    user_games[user_id] = {
        'current_attempt': 0,
        'attempts': attempts,
        'secret_number': secret_number,
        'range': range_num
    }

    await message.answer(f"Режим сложности: {get_description(difficulty)}\n"
                         f"У тебя есть <b>{attempts} попыток</b>\n"
                         f"Я загадал число в диапазоне <b>от 1 до {range_num}</b>, попробуй угадать!",
                         parse_mode='HTML',
                         reply_markup=get_during_game_menu())
    
    await message.answer('Введи какое-нибудь число')
    