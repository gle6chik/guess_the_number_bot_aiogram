from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import Bot
from ..keyboards.reply import get_start_menu
from states import UserStates
from commands.manager import CommandManager

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(UserStates.menu)

    if not message.from_user:
        await message.answer("Ошибка: невозможно определить пользователя")
        return
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu)

    GREET_STICKER_ID = 'CAACAgIAAxkBAAMDaVS6X1rRba6dWlSRsQLWwo3fuasAAj5PAAIXwFFJKUtKhmRzC3A4BA'
    await message.answer_sticker(GREET_STICKER_ID)
    await message.answer('Привет! Это игра "Угадай число"',
                         reply_markup=get_start_menu()
                         )
    
@router.message(Command('menu'), StateFilter(UserStates.menu))
async def cmd_change_menu(message: types.Message):
    await message.answer('Меню открыто',
                         reply_markup=get_start_menu()
                         )

@router.message(Command('help'), StateFilter(UserStates.menu))
async def cmd_help(message: types.Message):
    await message.answer('Тут будет что-то про навигацию по боту, я пока не придумал')
