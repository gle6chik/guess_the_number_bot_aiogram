from aiogram import Router, types, F
from bot.keyboards.menues import get_start_menu
from bot.keyboards.inline import get_choice_of_difficulty
from aiogram.types import ReplyKeyboardRemove

router = Router()

@router.message(F.text == 'Новая игра')
async def new_game_handler(message: types.Message):
    await message.answer('Выберите сложность игры',
                         reply_markup=get_choice_of_difficulty()
                         )
    
@router.message(F.text == 'Правила игры')
async def rules_handler(message: types.Message):
    await message.answer('Здесь будут описаны правила игры',
                         reply_markup=get_start_menu()
                         ) 

@router.message(F.text == 'О боте')
async def about_handler(message: types.Message):
    await message.answer('Здесь будет информация о боте',
                         reply_markup=get_start_menu()
                         )

@router.message(F.text == 'Скрыть меню')
async def hide_menu_handler(message: types.Message):
    await message.answer('Меню скрыто',
                         reply_markup=ReplyKeyboardRemove()
                         )
