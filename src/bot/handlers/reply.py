from aiogram import Router, types, F
from bot.keyboards.reply import get_persistent_menu, get_remove_menu

router = Router()

@router.message(F.text == 'Правила игры')
async def rules_handler(message: types.Message):
    await message.answer('Похоже, что всё-таки правила игры будут вот здесь)',
                         reply_markup=get_persistent_menu()
                         )
    print('Логи :)')
    
@router.message(F.text == 'Ещё что-нибудь')
async def else_handler(message: types.Message):
    await message.answer('Здесь можно написать всё что угодно :)',
                         reply_markup=get_persistent_menu()
                         )    

@router.message(F.text == 'Ну еще что-то')
async def else1_handler(message: types.Message):
    await message.answer('Привет сосед',
                         reply_markup=get_persistent_menu() # get_remove_menu() - тогда меню пропадёт после нажатия этой кнопки
                         ) 
