import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from bot.handlers.commands import router as commands_router
from bot.handlers.reply_before_game import router as reply_before_game_router
from bot.handlers.reply_during_game import router as reply_during_game_router
from bot.handlers.text import router as text_router
from bot.handlers.callbacks import router as callback_router

if TOKEN is None:
    raise ValueError('API_TOKEN не найден в переменных окружения')

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключение маршрутов к обработчикам
dp.include_router(commands_router)
dp.include_router(reply_before_game_router)
dp.include_router(reply_during_game_router)
dp.include_router(text_router)
dp.include_router(callback_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
