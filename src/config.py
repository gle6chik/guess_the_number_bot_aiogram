import os
from dotenv import load_dotenv

# Загрузка токена из переменной окружения
load_dotenv()
TOKEN = os.getenv('API_TOKEN')
