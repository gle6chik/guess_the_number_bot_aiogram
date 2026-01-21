from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import Bot
from ..keyboards.reply import get_start_menu
from ..keyboards.inline import get_cleaning_of_statistics, get_rating_information
from states import UserStates
from commands.manager import CommandManager
from text.text import MESSAGE
from database.database import UserDB, activity_checkpoint
from text.emoji import Emoji

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    activity_checkpoint(message)
    await state.set_state(UserStates.menu)
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu) # type: ignore

    GREET_STICKER_ID = 'CAACAgIAAxkBAAMDaVS6X1rRba6dWlSRsQLWwo3fuasAAj5PAAIXwFFJKUtKhmRzC3A4BA'
    await message.answer_sticker(GREET_STICKER_ID)
    await message.answer(MESSAGE['menu']['command']['start'],
                         parse_mode='HTML',
                         reply_markup=get_start_menu())

@router.message(Command('help'), StateFilter(UserStates.menu))
async def cmd_help(message: types.Message):
    activity_checkpoint(message)
    await message.answer(MESSAGE['menu']['command']['help'], parse_mode='HTML')

@router.message(Command('stat'), StateFilter(UserStates.menu))
async def cmd_stat(message: types.Message):
    activity_checkpoint(message)

    info = message.from_user
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

    await message.answer(f"<b>{Emoji.STATISTIC} Твоя статистика</b>\n\n"
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
    
@router.message(Command('top'), StateFilter(UserStates.menu))
async def cmd_top(message: types.Message):
    activity_checkpoint(message)

    db = UserDB()
    data = db.read_top_users()
    db.close()

    if not data:
        await message.answer(f"{Emoji.EXCLAMATION_MARK} Рейтинг не может быть составлен, так как никто из пользователей ни разу не угадал число.")
        return

    lines = ['ТОП 10 ИГРОКОВ:\n']
    for i, (name, games_won) in enumerate(data, start=1):
        lines.append(f"{i}. {name}: {games_won}")
    rating = '\n'.join(lines)
        
    await message.answer(rating, reply_markup=get_rating_information())