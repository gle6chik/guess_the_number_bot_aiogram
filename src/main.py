import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers.commands import router as commands_router

# Загрузка токена из переменной окружения
load_dotenv()
TOKEN = os.getenv('API_TOKEN')
if TOKEN is None:
    raise ValueError('API_TOKEN не найден в переменных окружения')

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 
dp.include_router(commands_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
