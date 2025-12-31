from aiogram import Router, types, F
from bot.keyboards.menues import get_start_menu
from bot.keyboards.inline import get_choice_of_difficulty

router = Router()

@router.message(F.text == 'Новая игра')
async def rules_handler(message: types.Message):
    await message.answer('Здесь будет выбор сложности',
                         reply_markup=get_choice_of_difficulty()
                         )
    print('Нажато: Новая игра')
    
@router.message(F.text == 'Правила игры')
async def else_handler(message: types.Message):
    await message.answer('Здесь будут описаны правила игры',
                         reply_markup=get_start_menu()
                         )   
    print('Нажато: Правила игры') 

@router.message(F.text == 'О боте')
async def else1_handler(message: types.Message):
    await message.answer('Здесь будет информация о боте',
                         reply_markup=get_start_menu()
                         )
    print('Нажато: О боте')
