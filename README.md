# guess_the_number_bot_aiogram

> **Educational Project Disclaimer:** This is a learning project created to practice Python and Telegram Bot API development. The code demonstrates working functionality but may contain simplified solutions and non-optimal patterns typical for educational code.

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/gle6chik/guess_the_number_bot_aiogram/releases/tag/v1.0.0)

## About the project
This bot implements the classic "Guess the Number" game in Telegram.

## Architecture description
This bot has two modes: **menu** and **game**.
In each mode, the user can use buttons and commands to control the bot and gameplay.

### Menu mode
1. Commands
+ `/start` - restart the bot
+ `/help` - show information about bot navigation
2. Buttons
+ *Новая игра* (New Game) - start a new game
    In this case, an inline keyboard will appear to select the game difficulty:
    - *Лёгкий* (Easy)
    - *Средний* (Medium) 
    - *Сложный* (Hard)
    - *Назад* (Back) - return to the main menu
+ *Правила игры* (Game Rules) - show rules of the game
+ *О боте* (About the Bot) - show information about the bot

### Game mode
1. Commands
+ `/start` - restart the bot
+ `/menu` - show menu bar
2. Buttons
+ *Выйти из игры* (Leave Game) - force quit the game
+ *Скрыть меню* (Hide Menu) - hide the menu bar

## Requirements
+ Python 3.10+
+ Telegram account
+ Bot token from [@BotFather](https://t.me/botfather)

## Installation
```bash
# Clone a repository
git clone git@github.com:gle6chik/guess_the_number_bot_aiogram.git
cd guess_the_number_bot_aiogram

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# For Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration
1. Get a bot token in [@BotFather](https://t.me/botfather)
2. Copy the configuration file
```bash
cd src
cp .env.example .env
```
3. Edit `.env` and add your token
```
API_TOKEN=your_bot_token_here
```
> **Important**: NEVER commit the `.env` file to version control! Ensure it's listed in your `.gitignore`.

## Launching
```bash
python3 main.py
```

---
**Project Status:** Under development | Educational project | Core gameplay complete
