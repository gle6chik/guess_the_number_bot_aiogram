from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards.menues import get_start_menu, get_second_menu

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMDaVS6X1rRba6dWlSRsQLWwo3fuasAAj5PAAIXwFFJKUtKhmRzC3A4BA')
    await message.answer('Привет! Это игра "Угадай число"',
                         reply_markup=get_start_menu()
                         )

@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('Тут, наверное, будут правила игры, но может быть я изменю название самой команды')

@router.message(Command('change_menu'))
async def cmd_change_menu(message: types.Message):
    await message.answer('Меню изменилось!',
                         reply_markup=get_second_menu()
                         )
