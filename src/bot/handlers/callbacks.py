from aiogram import Router, types, F
from game.main import game_process as play

router = Router()

@router.callback_query(F.data == 'start_easy')
async def easy_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбран режим сложности: Лёгкий') # type: ignore
    await play(callback.message, 'easy') # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_medium')
async def medium_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбран режим сложности: Средний') # type: ignore
    await play(callback.message, 'medium') # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_difficult')
async def difficult_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Выбран режим сложности: Сложный') # type: ignore
    await play(callback.message, 'difficult') # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'back')
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Вернулись назад') # type: ignore
    await callback.answer()
