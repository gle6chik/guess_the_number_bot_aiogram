from aiogram import Bot
from aiogram.fsm.state import State
from aiogram.types import BotCommandScopeChat
from .menu import get_menu_commands
from .game import get_game_commands
from states import UserStates

class CommandManager:
    @staticmethod
    async def set_commands_for_state(bot: Bot, user_id: int, state: State):
        scope = BotCommandScopeChat(chat_id=user_id)

        if state == UserStates.menu:
            commands = get_menu_commands()
        elif state == UserStates.game:
            commands = get_game_commands()
        
        await bot.set_my_commands(commands=commands, scope=scope)  
