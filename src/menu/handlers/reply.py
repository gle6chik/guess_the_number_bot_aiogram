from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import StateFilter
from ..keyboards.reply import get_start_menu
from ..keyboards.inline import get_choice_of_difficulty
from states import UserStates

router = Router()

@router.message(F.text == 'Новая игра', StateFilter(UserStates.menu))
async def new_game_handler(message: types.Message):
    await message.answer('Выбери сложность игры',
                         reply_markup=get_choice_of_difficulty()
                         )
    
@router.message(F.text == 'Правила игры', StateFilter(UserStates.menu))
async def rules_handler(message: types.Message):
    text = (
        '<b>Правила игры</b>\n\n'
        'В зависимости от выбранной сложности (<i>легко, средне, сложно</i>), <b>я загадаю число</b> в определенном диапазоне.\n\n'
        '<b>Твоя задача - отгадать</b> это число за ограниченное количество попыток.\n\n'
        'Желаю удачи!'
    )
    await message.answer(text, parse_mode='HTML', reply_markup=get_start_menu()) 

@router.message(F.text == 'О боте', StateFilter(UserStates.menu))
async def about_handler(message: types.Message):
    await message.answer('<a href="https://github.com/gle6chik/guess_the_number_bot_aiogram">Ссылка на репозиторий GitHub</a>',
                         parse_mode='HTML',
                         reply_markup=get_start_menu()
                         )
