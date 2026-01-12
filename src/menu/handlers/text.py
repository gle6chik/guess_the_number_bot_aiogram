from aiogram import Router, types, F
from aiogram.filters import StateFilter
from states import UserStates

router = Router()

@router.message(F.text, StateFilter(UserStates.menu))
async def text_handler(message: types.Message):
    await message.answer('Чтобы сыграть, нажми "Новая игра"\nЧтобы посмотреть все действия, напиши /help')
