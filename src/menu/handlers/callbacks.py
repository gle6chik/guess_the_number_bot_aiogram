from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from game.logic import start_game as play
from states import UserStates
from commands.manager import CommandManager

router = Router()

@router.callback_query(F.data == 'start_easy', StateFilter(UserStates.menu))
async def easy_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    print(f"CALLBACK easy: user_id={callback.from_user.id}, username={callback.from_user.username}")
    await callback.message.edit_text('Выбран режим сложности: Лёгкий') # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'easy', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_medium', StateFilter(UserStates.menu))
async def medium_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.edit_text('Выбран режим сложности: Средний') # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'medium') # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_difficult')
async def difficult_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.edit_text('Выбран режим сложности: Сложный') # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'difficult') # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'back', StateFilter(UserStates.menu))
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Вернулись назад') # type: ignore
    await callback.answer()
