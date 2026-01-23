from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters import StateFilter
from bot.states import UserStates
from bot.game.keyboards.reply import get_during_game_menu
from bot.text import text
from bot.database.database import activity_checkpoint

router = Router()

@router.message(Command('menu'), StateFilter(UserStates.game))
async def cmd_change_menu(message: types.Message):
    activity_checkpoint(message)
    await message.answer(text.GAME_CMD_CHANGEMENU, reply_markup=get_during_game_menu())
