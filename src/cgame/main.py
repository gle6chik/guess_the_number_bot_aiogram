from aiogram import types
from bot.keyboards.menues import get_during_game_menu
from cgame.difficulties import get_attempts, get_range

async def game_process(message: types.Message, difficulty: str):
    await message.answer('Игра началась', reply_markup=get_during_game_menu())
    await message.answer(f"Попыток: {get_attempts(difficulty)}\nДиапазон: {get_range(difficulty)}")

    ATTEMPTS = get_attempts(difficulty)
    RANGE = get_range(difficulty)

    for i in range(1, ATTEMPTS + 1):
        await message.answer(f"Число: {i}")