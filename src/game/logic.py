from aiogram import types
from .keyboards.reply import get_during_game_menu
from .difficulties import get_attempts, get_range

async def game_process(message: types.Message, difficulty: str):
    await message.answer(f"Сложность: {difficulty}"
                         f"Попыток: {get_attempts(difficulty)}\n"
                         f"Диапазон: {get_range(difficulty)}",
                         reply_markup=get_during_game_menu())
    await message.answer('Введите число')

    ATTEMPTS = get_attempts(difficulty)
    RANGE = get_range(difficulty)

    
    