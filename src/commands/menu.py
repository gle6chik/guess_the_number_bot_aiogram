from aiogram.types import BotCommand

def get_menu_commands():
    return [
        BotCommand(command='/start', description='Перезапустить бота'),
        BotCommand(command='/help', description='Помощь'),
        BotCommand(command='/test', description='test')
    ]
