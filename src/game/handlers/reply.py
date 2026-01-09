from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from menu.keyboards.reply import get_start_menu
from states import UserStates

router = Router()

@router.message(F.text == 'Выйти из игры', StateFilter(UserStates.game))
async def leave_game_handler(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.menu)
    await message.answer('Игра остановлена',
                         reply_markup=get_start_menu()
                         )
