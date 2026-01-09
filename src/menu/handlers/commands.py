from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from ..keyboards.reply import get_start_menu
from states import UserStates

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.menu)
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
