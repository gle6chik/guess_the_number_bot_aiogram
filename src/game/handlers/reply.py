from aiogram import Router, types, F
from menu.keyboards.reply import get_start_menu

router = Router()

@router.message(F.text == 'Выйти из игры')
async def leave_game_handler(message: types.Message):
    await message.answer('Игра остановлена',
                         reply_markup=get_start_menu()
                         )
