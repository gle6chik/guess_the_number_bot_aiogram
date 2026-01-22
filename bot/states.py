from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

class UserStates(StatesGroup):
    menu = State()
    game = State()

STORAGE = MemoryStorage()
