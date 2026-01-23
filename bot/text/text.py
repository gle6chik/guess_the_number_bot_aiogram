from bot.text.emoji import Emoji

# Menu
# Commands
MENU_CMD_START = (f"""
Привет! {Emoji.GREET}
Это игра <b>"Угадай число"</b>
Готов проверить свою интуицию? {Emoji.WINK}
""")
MENU_CMD_HELP = (f"""
{Emoji.COMPASS} <b>Навигация по боту</b>


Ты можешь воспользоваться кнопками и командами


{Emoji.MENU} <b>Меню</b>
1. Кнопки {Emoji.BUTTON}
   {Emoji.MARKER} Правила игры - описание правил игры
   {Emoji.MARKER} О боте - техническая информация о боте (для разработчиков)
   {Emoji.MARKER} Новая игра - начать новую игру
2. Команды {Emoji.COMMAND}
   {Emoji.MARKER} /start - перезапустить бота
   {Emoji.MARKER} /help - открыть информацию о навигации по боту (данная справка)
   {Emoji.MARKER} /stat - открыть информацию об активности пользователя
   {Emoji.MARKER} /top - открыть рейтинг игроков


{Emoji.GAME} <b>Игра</b>
1. Кнопки {Emoji.BUTTON}
   {Emoji.MARKER} Выйти из игры - принудительно закончить игру
   {Emoji.MARKER} Скрыть меню - убрать меню снизу
2. Команды {Emoji.COMMAND}
   {Emoji.MARKER} /start - перезапустить бота
   {Emoji.MARKER} /menu - показать меню внизу экрана
""")
MENU_CMD_STAT = (
    lambda 
    easy_best_result,
    medium_best_result,
    hard_best_result,
    easy_games_played,
    medium_games_played,
    hard_games_played,
    total_games_played,
    winning_percentage,
    losing_percentage:
    (f"""
<b>{Emoji.STATISTIC} Твоя статистика</b>

{Emoji.MARKER} Сыграно игр в режиме <i>Легко</i>: {easy_games_played}
{Emoji.MARKER} Сыграно игр в режиме <i>Средне</i>: {medium_games_played}
{Emoji.MARKER} Сыграно игр в режиме <i>Сложно</i>: {hard_games_played}

{Emoji.MARKER} Рекорд в режиме <i>Легко</i>: {easy_best_result}
{Emoji.MARKER} Рекорд в режиме <i>Средне</i>: {medium_best_result}
{Emoji.MARKER} Рекорд в режиме <i>Сложно</i>: {hard_best_result}

{Emoji.MARKER} Всего сыграно игр: {total_games_played}

{Emoji.MARKER} Процент выигрышей: {winning_percentage}%
{Emoji.MARKER} Процент проигрышей: {losing_percentage}%
""")
)
MENU_CMD_RATINGNOTEXISTS = f"{Emoji.EXCLAMATION_MARK} Рейтинг не может быть составлен, так как никто из пользователей ни разу не угадал число."
MENU_CMD_TOPTITLE = f"{Emoji.TROPHY} ТОП 10 ИГРОКОВ:\n"

# Callbacks
MENU_CLB_BACK = 'Нажми "Новая игра", чтобы сыграть!'
MENU_CLB_CONFIRMSTATCLEAN = (f"""
{Emoji.EXCLAMATION_MARK} ВНИМАНИЕ {Emoji.EXCLAMATION_MARK}

Ты уверен, что хочешь сбросить свою статистику? Это действие необратимо, оно удалит тебя из общего рейтинга.

Удалить статистику?
""")
MENU_CLB_CONFIRMSTATCLEANYES = 'Статистика сброшена.'
MENU_CLB_CONFIRMSTATCLEANNO = MENU_CMD_STAT
MENU_CLB_ABOUTRATING = (f"""
Этот рейтинг отображает 10 лучших игроков в "Угадай число", у которых больше всего выигрышей {Emoji.TROPHY}

Выигрывай больше, чтобы попасть в десятку лучших! {Emoji.WINK}
""")

# Reply
MENU_RPL_NEWGAME = f"Выбери сложность игры {Emoji.HAND_DOWN}"
MENU_RPL_RULES = (f"""
{Emoji.BOOK} <b>Правила игры</b>


В зависимости от выбранной сложности (<i>легко, средне, сложно</i>),
<b>я загадаю число</b> в определенном диапазоне {Emoji.NUMBERS}

{Emoji.QUESTION_MARK} <b>Твоя задача - отгадать</b> это число за ограниченное количество попыток
Желаю удачи! {Emoji.COOL_FACE}
""")
MENU_RPL_ABOUT = '<a href="https://github.com/gle6chik/guess_the_number_bot_aiogram">Ссылка на репозиторий GitHub</a>'

# Text
MENU_TXT_TEXT = 'Чтобы сыграть, нажми "Новая игра"\nЧтобы посмотреть все действия, напиши /help'


# Game
# Commands
GAME_CMD_CHANGEMENU = 'Меню открыто.\nПродолжаем игру.'

# Reply
GAME_RPL_ENDGAME = 'Игра окончена.'
GAME_RPL_HIDEMENU = 'Меню скрыто.\nПродолжаем игру.'

# Text
GAME_TXT_TEXTONLY = f"{Emoji.EXCLAMATION_MARK} Здесь нужно писать только числа"

# Logic
GAME_LOG_WIN = (
    lambda current_attempt, attempts, secret_num:
    f"Победа!\nПопытка: {current_attempt} / {attempts}\nТы молодец! {Emoji.LIKE}\nЗагаданное число: {secret_num}"
)
GAME_LOG_LOSE = (
    lambda secret_num:
    f"{Emoji.SAD_FACE} Количество попыток закончилось...\nЗагаданное число - {secret_num}\nНе переживай, в следующий раз повезёт! {Emoji.HUNDRED}"
)
GAME_LOG_MORE = (
    lambda number, attempts_left:
    f"Загаданное число БОЛЬШЕ {number}\nПопыток осталось: {attempts_left}"
)
GAME_LOG_LESS = (
    lambda number, attempts_left:
    f"Загаданное число МЕНЬШЕ {number}\nПопыток осталось: {attempts_left}"
)
GAME_LOG_STARTGAME = (
    lambda difficulty, attempts, range_num: (f"""
Режим сложности: {difficulty}
У тебя есть <b>{attempts} попыток</b>
Я загадал число в диапазоне
<b>от 1 до {range_num}</b>
Попробуй угадать! {Emoji.WINK}
""")
)
GAME_LOG_OUTRANGE = f"{Emoji.EXCLAMATION_MARK} Это число вне диапазона! Попробуй другое."
GAME_LOG_ENTERNUMBER = 'Введи какое-нибудь число.'
