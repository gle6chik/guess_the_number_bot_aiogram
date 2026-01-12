from aiogram.types import BotCommand

def get_game_commands():
    return [
        BotCommand(command='/start', description='Перезапустить бота'),
        BotCommand(command='/menu', description='Показать меню')
    ]
