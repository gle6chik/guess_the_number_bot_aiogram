from aiogram import Router, types, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from states import UserStates
from game import logic
from ..handlers.reply import leave_game_handler as game_over

router = Router()

@router.message(F.text, StateFilter(UserStates.game))
async def text_handler(message: types.Message, state: FSMContext, bot: Bot):
    text = message.text

    if text.isdigit(): # type: ignore
        number = int(text) # type: ignore
        response, end_code = logic.game(number) # type: ignore
        await message.answer(response) # type: ignore

        if end_code == 1:
            await game_over(message, state, bot)
    else:
        await message.answer('Здесь нужно писать только числа')
