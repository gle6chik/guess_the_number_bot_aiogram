from aiogram import types
from bot.keyboards.menues import get_during_game_menu

async def game_process(message: types.Message, difficulty: str):
    await message.answer('Должно работать!!!\n' + difficulty,
                         reply_markup=get_during_game_menu()
                         )
