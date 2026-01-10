import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from states import STORAGE

from menu.handlers.commands import router as mr_cmd
from menu.handlers.callbacks import router as mr_clb
from menu.handlers.reply import router as mr_rpl
from menu.handlers.text import router as mr_txt

from game.handlers.commands import router as gr_cmd
from game.handlers.reply import router as gr_rpl
from game.handlers.text import router as gr_txt

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
