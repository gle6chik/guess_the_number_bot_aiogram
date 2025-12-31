from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Это игра "Угадай число"')

@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer('Тут, наверное, будут правила игры, но может быть я изменю название самой команды')

@router.message(Command('greet'))
async def cmd_greet(message: types.Message):
    await message.answer('Это СУПЕРПРИВЕТ!!!')
