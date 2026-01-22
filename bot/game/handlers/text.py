from aiogram import Router, types, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
import time
from states import UserStates
from game import logic
from ..handlers.reply import leave_game_handler as game_over
from text import text
from text.emoji import Emoji
from database.database import activity_checkpoint

router = Router()

@router.message(F.text, StateFilter(UserStates.game))
async def text_handler(message: types.Message, state: FSMContext, bot: Bot):
    activity_checkpoint(message)
    
    user_id = message.from_user.id # type: ignore
    user_text = message.text

    if user_text.isdigit(): # type: ignore
        number = int(user_text) # type: ignore
        response, end_code = logic.game(user_id, number) # type: ignore
        await message.answer(response) # type: ignore

        if end_code == 2: # win
            await message.react([types.ReactionTypeEmoji(emoji=Emoji.PARTY_POPPER)])
            time.sleep(1)
            await game_over(message, state, bot)
        elif end_code == 1: # lose
            await game_over(message, state, bot)
    else:
        await message.answer(text.GAME_TXT_TEXTONLY)
