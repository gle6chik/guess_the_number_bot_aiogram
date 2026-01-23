from aiogram import Router, types, F
from aiogram.filters import StateFilter
from bot.states import UserStates
from bot.text import text
from bot.database.database import activity_checkpoint

router = Router()

@router.message(F.text, StateFilter(UserStates.menu))
async def text_handler(message: types.Message):
    activity_checkpoint(message)
    await message.answer(text.MENU_TXT_TEXT)
