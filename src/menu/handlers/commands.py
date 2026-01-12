from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import Bot
from ..keyboards.reply import get_start_menu
from states import UserStates
from commands.manager import CommandManager

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext, bot: Bot):
    await state.set_state(UserStates.menu)
    await CommandManager.set_commands_for_state(bot, message.from_user.id, UserStates.menu) # type: ignore

    GREET_STICKER_ID = 'CAACAgIAAxkBAAMDaVS6X1rRba6dWlSRsQLWwo3fuasAAj5PAAIXwFFJKUtKhmRzC3A4BA'
    await message.answer_sticker(GREET_STICKER_ID)
    await message.answer('Привет! Это игра <b>"Угадай число"</b>\n'
                         'Готов проверить свою интуицию?',
                         parse_mode='HTML',
                         reply_markup=get_start_menu()
                         )

@router.message(Command('help'), StateFilter(UserStates.menu))
async def cmd_help(message: types.Message):
    MARKER_CODE = '\u2022'
    text = (
        '<b>Навигация по боту</b>\n\n'
        'Есть два режима: <b>Меню</b> и <b>Игра</b>\n'
        'Ты можешь воспользоваться кнопками и командами\n\n'
        '<b>Меню</b>\n'
        '1. Кнопки\n'
        f"   {MARKER_CODE} Правила игры - описание правил игры\n"
        f"   {MARKER_CODE} О боте - техническая информация о боте (для разработчиков)\n"
        f"   {MARKER_CODE} Новая игра - начать новую игру\n"
        '2. Команды\n'
        f"   {MARKER_CODE} /start - перезапустить бота\n"
        f"   {MARKER_CODE} /help - открыть информацию о навигации по боту (данная справка)\n"
        f"   {MARKER_CODE} /test - test\n\n"
        '<b>Игра</b>\n'
        '1. Кнопки\n'
        f"   {MARKER_CODE} Выйти из игры - принудительно закончить игру\n"
        f"   {MARKER_CODE} Скрыть меню - убрать меню снизу\n\n"
        '2. Команды\n'
        f"   {MARKER_CODE} /start - перезапустить бота\n"
        f"   {MARKER_CODE} /menu - показать меню внизу экрана\n"
        f"   {MARKER_CODE} /test - test\n\n"
    )
    await message.answer(text, parse_mode='HTML')
