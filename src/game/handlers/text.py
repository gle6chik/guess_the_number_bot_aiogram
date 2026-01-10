from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from states import UserStates
from game import logic

router = Router()

@router.message(F.text, StateFilter(UserStates.game))
async def text_handler(message: types.Message):
    text = message.text

    if text.isdigit(): # type: ignore
        number = int(text) # type: ignore
        response = logic.game(number)
        await message.answer(response)
    else:
        await message.answer('Здесь нужно писать только числа')
