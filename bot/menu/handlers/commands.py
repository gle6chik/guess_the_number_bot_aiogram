from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import Bot
from bot.menu.keyboards.reply import get_start_menu
from bot.menu.keyboards.inline import get_cleaning_of_statistics, get_rating_information
from bot.states import UserStates
from bot.commands.manager import CommandManager
from bot.text import text
from bot.database.database import UserDB, activity_checkpoint
from bot.text.emoji import Emoji

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    activity_checkpoint(message)
    await state.set_state(UserStates.menu)
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu) # type: ignore

    GREET_STICKER_ID = 'CAACAgIAAxkBAAMDaVS6X1rRba6dWlSRsQLWwo3fuasAAj5PAAIXwFFJKUtKhmRzC3A4BA'
    await message.answer_sticker(GREET_STICKER_ID)
    await message.answer(text.MENU_CMD_START,
                         parse_mode='HTML',
                         reply_markup=get_start_menu())

@router.message(Command('help'), StateFilter(UserStates.menu))
async def cmd_help(message: types.Message):
    activity_checkpoint(message)
    await message.answer(text.MENU_CMD_HELP, parse_mode='HTML')

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

    await message.answer(
        text.MENU_CMD_STAT(
            easy_best_result,
            medium_best_result,
            hard_best_result,
            easy_games_played,
            medium_games_played,
            hard_games_played,
            total_games_played,
            winning_percentage,
            losing_percentage),
            parse_mode='HTML',
            reply_markup=get_cleaning_of_statistics())
    
@router.message(Command('top'), StateFilter(UserStates.menu))
async def cmd_top(message: types.Message):
    activity_checkpoint(message)

    db = UserDB()
    data = db.read_top_users()
    db.close()

    if not data:
        await message.answer(text.MENU_CMD_RATINGNOTEXISTS)
        return

    lines = [text.MENU_CMD_TOPTITLE]
    for i, (name, games_won) in enumerate(data, start=1):
        index = None
        if i == 1: index = Emoji.FIRST_PLACE_MEDAL
        elif i == 2: index = Emoji.SECOND_PLACE_MEDAL
        elif i == 3: index = Emoji.THIRD_PLACE_MEDAL
        else: index = str(i)+'.'
        lines.append(f"{index} {name}: {games_won}")
    rating = '\n'.join(lines)
        
    await message.answer(rating, reply_markup=get_rating_information())