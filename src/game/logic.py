from aiogram import types

async def game_process(message: types.Message, difficulty: str):
    await message.answer(f"Сложность: {difficulty}")