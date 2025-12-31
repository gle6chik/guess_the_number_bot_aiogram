import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.commands import router as commands_router
from bot.handlers.reply import router as reply_router
from bot.handlers.text import router as text_router

# Загрузка токена из переменной окружения
load_dotenv()
TOKEN = os.getenv('API_TOKEN')
if TOKEN is None:
    raise ValueError('API_TOKEN не найден в переменных окружения')

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключение маршрутов к обработчикам
dp.include_router(commands_router)
dp.include_router(reply_router)
dp.include_router(text_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
