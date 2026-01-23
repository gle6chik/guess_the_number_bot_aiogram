import sys
import os

# Получение абсолютного путя к этому файлу
current_file = os.path.abspath(__file__)  # /guess_the_number_bot/bot/main.py
current_dir = os.path.dirname(current_file)  # /guess_the_number_bot/bot

# Добавление корня проекта в sys.path
project_root = os.path.dirname(current_dir)  # /guess_the_number_bot
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Добавление bot/ в путь для импортов внутри bot/
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from states import STORAGE

from bot.menu.handlers.commands import router as mr_cmd
from bot.menu.handlers.callbacks import router as mr_clb
from bot.menu.handlers.reply import router as mr_rpl
from bot.menu.handlers.text import router as mr_txt

from bot.game.handlers.commands import router as gr_cmd
from bot.game.handlers.reply import router as gr_rpl
from bot.game.handlers.text import router as gr_txt

if TOKEN is None:
    raise ValueError('API_TOKEN не найден в переменных окружения')

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=STORAGE)

# Подключение маршрутов к обработчикам
dp.include_router(mr_cmd)
dp.include_router(mr_clb)
dp.include_router(mr_rpl)
dp.include_router(mr_txt)

dp.include_router(gr_cmd)
dp.include_router(gr_rpl)
dp.include_router(gr_txt)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
