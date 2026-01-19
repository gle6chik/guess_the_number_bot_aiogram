from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from game.logic import start_game as play
from states import UserStates
from commands.manager import CommandManager
from text.text import MESSAGE

router = Router()

@router.callback_query(F.data == 'start_easy', StateFilter(UserStates.menu))
async def easy_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.delete() # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'easy', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_medium', StateFilter(UserStates.menu))
async def medium_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.delete() # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'medium', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_hard')
async def difficult_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.delete() # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'hard', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'back', StateFilter(UserStates.menu))
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(MESSAGE['menu']['callback']['back']) # type: ignore
    await callback.answer()
