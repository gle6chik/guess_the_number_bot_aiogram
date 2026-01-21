from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters import StateFilter
from states import UserStates
from ..keyboards.reply import get_during_game_menu
from text.text import MESSAGE
from database.database import activity_checkpoint

router = Router()

@router.message(Command('menu'), StateFilter(UserStates.game))
async def cmd_change_menu(message: types.Message):
    activity_checkpoint(message)
    await message.answer(MESSAGE['game']['command']['change_menu'], reply_markup=get_during_game_menu())
