from aiogram import types
import random
from bot.game.keyboards.reply import get_during_game_menu
from bot.game.difficulties import get_description, get_attempts, get_range
from bot.text import text
from bot.database.database import UserDB

user_games = {}

def game(user_id: int, number: int):
    game_data = user_games[user_id]
    game_data['current_attempt'] += 1

    if number == game_data['secret_number']:
        del user_games[user_id]

        db = UserDB()
        db.write_statistic(game_data['difficulty'], user_id, game_data['current_attempt'], True)
        db.close()

        return text.GAME_LOG_WIN(game_data['current_attempt'],
                                               game_data['attempts'],
                                               game_data['secret_number']), 2

    if game_data['current_attempt'] >= game_data['attempts']:
        del user_games[user_id]

        db = UserDB()
        db.write_statistic(game_data['difficulty'], user_id, 0, False)
        db.close()

        return text.GAME_LOG_LOSE(game_data['secret_number']), 1
    
    if number < 1 or number > game_data['range']:
        game_data['current_attempt'] -= 1
        return text.GAME_LOG_OUTRANGE, 0
    
    elif number < game_data['secret_number']:
        attempts_left = game_data['attempts'] - game_data['current_attempt']
        return text.GAME_LOG_MORE(number, attempts_left), 0
    elif number > game_data['secret_number']:
        attempts_left = game_data['attempts'] - game_data['current_attempt']

        return text.GAME_LOG_LESS(number, attempts_left), 0

async def start_game(message: types.Message, difficulty: str, user_id: int):
    attempts = get_attempts(difficulty=difficulty)
    range_num = get_range(difficulty=difficulty)
    secret_number = random.randint(1, range_num)

    user_games[user_id] = {
        'current_attempt': 0,
        'attempts': attempts,
        'secret_number': secret_number,
        'range': range_num,
        'difficulty': difficulty
    }

    await message.answer(text.GAME_LOG_STARTGAME(
        get_description(difficulty),
        attempts,
        range_num),
        parse_mode='HTML',
        reply_markup=get_during_game_menu())
    
    await message.answer(text.GAME_LOG_ENTERNUMBER)
    