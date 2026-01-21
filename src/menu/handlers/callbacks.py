from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from game.logic import start_game as play
from states import UserStates
from commands.manager import CommandManager
from text.text import MESSAGE
from database.database import UserDB
from ..keyboards.inline import get_statistics_cleaning_confirmation, get_cleaning_of_statistics
from text.emoji import Emoji

router = Router()

@router.callback_query(F.data == 'start_easy', StateFilter(UserStates.menu))
async def start_easy_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.delete() # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'easy', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_medium', StateFilter(UserStates.menu))
async def start_medium_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.delete() # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'medium', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'start_hard')
async def start_hard_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    await callback.message.delete() # type: ignore
    await state.set_state(UserStates.game)
    await CommandManager.set_commands_for_state(bot, callback.from_user.id, UserStates.game)
    await play(callback.message, 'hard', user_id=callback.from_user.id) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'back', StateFilter(UserStates.menu))
async def back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(MESSAGE['menu']['callback']['back']) # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'clean_statistics', StateFilter(UserStates.menu))
async def clean_statistics_handler(callback: types.CallbackQuery):
    await callback.message.edit_text('Ты уверен, что хочешь сбросить свою статистику?\n' # type: ignore
                                     'Это действие необратимо, оно удалит тебя из общего рейтинга.\n'
                                     'Удалить статистику?',
                                     reply_markup=get_statistics_cleaning_confirmation())
    await callback.answer()

@router.callback_query(F.data == 'clean_confirm_yes', StateFilter(UserStates.menu))
async def clean_confirm_yes_handler(callback: types.CallbackQuery):
    db = UserDB()
    db.delete_statistics(callback.from_user.id)
    db.close()
    await callback.message.edit_text('Статистика сброшена') # type: ignore
    await callback.answer()

@router.callback_query(F.data == 'clean_confirm_no', StateFilter(UserStates.menu))
async def clean_confirm_no_handler(callback: types.CallbackQuery):
    info = callback.from_user
    db = UserDB()
    (easy_best_result,
    medium_best_result,
    hard_best_result,
    easy_games_played,
    medium_games_played,
    hard_games_played,
    total_games_played,
    winning_percentage,
    losing_percentage) = db.read_statistic(info.id) # type: ignore
    db.close()

    await callback.message.edit_text(f"<b>{Emoji.STATISTIC} Твоя статистика</b>\n\n" # type: ignore
                         f"{Emoji.MARKER} Сыграно игр в режиме <i>Легко</i>: {easy_games_played}\n"
                         f"{Emoji.MARKER} Сыграно игр в режиме <i>Средне</i>: {medium_games_played}\n"
                         f"{Emoji.MARKER} Сыграно игр в режиме <i>Сложно</i>: {hard_games_played}\n\n"
                         f"{Emoji.MARKER} Рекорд в режиме <i>Легко</i>: {easy_best_result}\n"
                         f"{Emoji.MARKER} Рекорд в режиме <i>Средне</i>: {medium_best_result}\n"
                         f"{Emoji.MARKER} Рекорд в режиме <i>Сложно</i>: {hard_best_result}\n\n"
                         f"{Emoji.MARKER} Всего сыграно игр: {total_games_played}\n\n"
                         f"{Emoji.MARKER} Процент выигрышей: {winning_percentage}%\n"
                         f"{Emoji.MARKER} Процент проигрышей: {losing_percentage}%",
                         parse_mode='HTML', reply_markup=get_cleaning_of_statistics())

    await callback.answer()

@router.callback_query(F.data == 'about_rating', StateFilter(UserStates.menu))
async def about_rating_handler(callback: types.CallbackQuery):
    await callback.answer('Этот рейтинг отображает 10 лучших игроков в "Угадай число", которые выиграли больше всего игр.\n\n'
                          'Выигрывай больше, чтобы попасть на первое место!', show_alert=True)
