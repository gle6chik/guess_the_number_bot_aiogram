from aiogram import Router, types, F
from aiogram.filters import StateFilter
from states import UserStates
from text.text import MESSAGE

router = Router()

@router.message(F.text, StateFilter(UserStates.menu))
async def text_handler(message: types.Message):
    await message.answer(MESSAGE['menu']['text']['text'])
