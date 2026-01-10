from aiogram import Router, types, F
from aiogram.filters import StateFilter
from states import UserStates

router = Router()

@router.message(F.text, StateFilter(UserStates.menu))
async def text_handler(message: types.Message):
    text = message.text

    await message.answer(f"Мы находимся в режиме МЕНЮ\nТы написал: {text}")

    if text.isdigit(): # type: ignore
        number = int(text) # type: ignore
        await message.answer(f"И кстати, {number} - это число")
    else:
        await message.answer(f"{text} - это не число")
