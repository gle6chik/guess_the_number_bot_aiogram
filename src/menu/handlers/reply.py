from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import StateFilter
from ..keyboards.reply import get_start_menu
from ..keyboards.inline import get_choice_of_difficulty
from states import UserStates

router = Router()

@router.message(F.text == 'Новая игра', StateFilter(UserStates.menu))
async def new_game_handler(message: types.Message):
    await message.answer('Выберите сложность игры',
                         reply_markup=get_choice_of_difficulty()
                         )
    
@router.message(F.text == 'Правила игры', StateFilter(UserStates.menu))
async def rules_handler(message: types.Message):
    await message.answer('Здесь будут описаны правила игры',
                         reply_markup=get_start_menu()
                         ) 

@router.message(F.text == 'О боте', StateFilter(UserStates.menu))
async def about_handler(message: types.Message):
    await message.answer('Здесь будет информация о боте',
                         reply_markup=get_start_menu()
                         )

@router.message(F.text == 'Скрыть меню', StateFilter(UserStates.menu))
async def hide_menu_handler(message: types.Message):
    await message.answer('Меню скрыто',
                         reply_markup=ReplyKeyboardRemove()
                         )
