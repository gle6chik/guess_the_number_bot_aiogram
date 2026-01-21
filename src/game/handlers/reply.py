from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import ReplyKeyboardRemove
from menu.keyboards.reply import get_start_menu
from states import UserStates
from commands.manager import CommandManager
from game import logic
from text.text import MESSAGE
from database.database import activity_checkpoint

router = Router()

@router.message(F.text == 'Выйти из игры', StateFilter(UserStates.game))
async def leave_game_handler(message: types.Message, state: FSMContext, bot: Bot):
    activity_checkpoint(message)

    await state.set_state(UserStates.menu)
    user_id = message.from_user.id # type: ignore

    # Удаление пользователя из игры при выходе
    if user_id in logic.user_games:
        del logic.user_games[user_id]

    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu) # type: ignore

    await message.answer(MESSAGE['game']['reply']['end_game'], reply_markup=get_start_menu())

@router.message(F.text == 'Скрыть меню', StateFilter(UserStates.game))
async def hide_menu_handler(message: types.Message):
    activity_checkpoint(message)
    await message.answer(MESSAGE['game']['reply']['hide_menu'], reply_markup=ReplyKeyboardRemove())
