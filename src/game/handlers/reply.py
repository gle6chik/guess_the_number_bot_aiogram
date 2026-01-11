from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import ReplyKeyboardRemove
from menu.keyboards.reply import get_start_menu
from states import UserStates
from commands.manager import CommandManager

number = 0
def get_number():
    global number
    return number

router = Router()

@router.message(F.text == 'Выйти из игры', StateFilter(UserStates.game))
async def leave_game_handler(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(UserStates.menu)

    if not message.from_user:
        await message.answer("Ошибка: невозможно определить пользователя")
        return
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu)

    await message.answer('Игра окончена',
                         reply_markup=get_start_menu()
                         )

@router.message(F.text == 'Скрыть меню', StateFilter(UserStates.game))
async def hide_menu_handler(message: types.Message):
    await message.answer('Меню скрыто\nПродолжаем игру',
                         reply_markup=ReplyKeyboardRemove()
                         )
