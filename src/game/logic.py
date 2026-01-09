from aiogram import types
from .keyboards.reply import get_during_game_menu

async def game_process(message: types.Message, difficulty: str):
    await message.answer(f"Сложность: {difficulty}", reply_markup=get_during_game_menu())