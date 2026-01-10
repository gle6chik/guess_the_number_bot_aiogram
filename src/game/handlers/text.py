from aiogram import Router, types, F
from aiogram.filters import StateFilter
from states import UserStates

router = Router()

async def test(message: types.Message):
    await message.answer('Работает')


@router.message(F.text, StateFilter(UserStates.game))
async def text_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}\nПроверки на число не будет, потому что это режим ИГРЫ")
    await test(message)
