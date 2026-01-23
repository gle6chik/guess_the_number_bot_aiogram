from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import StateFilter
from bot.menu.keyboards.reply import get_start_menu
from bot.menu.keyboards.inline import get_choice_of_difficulty
from bot.states import UserStates
from bot.text import text
from bot.text.emoji import Emoji
from bot.database.database import activity_checkpoint

router = Router()

@router.message(F.text == 'Новая игра', StateFilter(UserStates.menu))
async def new_game_handler(message: types.Message):
    activity_checkpoint(message)
    await message.answer(text.MENU_RPL_NEWGAME,
                         reply_markup=get_choice_of_difficulty())
    
@router.message(F.text == 'Правила игры', StateFilter(UserStates.menu))
async def rules_handler(message: types.Message):
    activity_checkpoint(message)
    await message.answer(text.MENU_RPL_RULES,
                         parse_mode='HTML',
                         reply_markup=get_start_menu()) 

@router.message(F.text == 'О боте', StateFilter(UserStates.menu))
async def about_handler(message: types.Message):
    activity_checkpoint(message)
    await message.react([types.ReactionTypeEmoji(emoji=Emoji.LIGHTNING)])
    await message.answer(text.MENU_RPL_ABOUT,
                         parse_mode='HTML',
                         reply_markup=get_start_menu())
