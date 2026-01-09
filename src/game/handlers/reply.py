from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from menu.keyboards.reply import get_start_menu
from states import UserStates
from commands.manager import CommandManager

router = Router()

@router.message(F.text == 'Выйти из игры', StateFilter(UserStates.game))
async def leave_game_handler(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(UserStates.menu)

    if not message.from_user:
        await message.answer("Ошибка: невозможно определить пользователя")
        return
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu)

    await message.answer('Игра остановлена',
                         reply_markup=get_start_menu()
                         )
