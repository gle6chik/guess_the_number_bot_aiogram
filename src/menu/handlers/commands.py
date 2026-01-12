from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import Bot
from ..keyboards.reply import get_start_menu
from states import UserStates
from commands.manager import CommandManager
from text.text import MESSAGE

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(UserStates.menu)
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu) # type: ignore

    GREET_STICKER_ID = 'CAACAgIAAxkBAAMDaVS6X1rRba6dWlSRsQLWwo3fuasAAj5PAAIXwFFJKUtKhmRzC3A4BA'
    await message.answer_sticker(GREET_STICKER_ID)
    await message.answer(MESSAGE['menu']['command']['start'],
                         parse_mode='HTML',
                         reply_markup=get_start_menu())

@router.message(Command('help'), StateFilter(UserStates.menu))
async def cmd_help(message: types.Message):
    await message.answer(MESSAGE['menu']['command']['help'], parse_mode='HTML')
