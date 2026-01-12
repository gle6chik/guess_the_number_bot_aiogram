from .emoji import Emoji

MESSAGE = {
    'menu': {
        'callback': {
            'back': 'Нажми "Новая игра", чтобы сыграть!'
        },
        'command': {
            'start': (
                f"Привет! {Emoji.GREET} Это игра <b>\"Угадай число\"</b>\n"
                f"Готов проверить свою интуицию? {Emoji.WINK}"
            ),
            'help': (
                f"<b>Навигация по боту</b> {Emoji.COMPASS}\n\n"
                'Есть два режима: <b>Меню</b> и <b>Игра</b>\n'
                'Ты можешь воспользоваться кнопками и командами\n\n'
                f"<b>Меню</b> {Emoji.MENU}\n"
                f"1. Кнопки {Emoji.BUTTON}\n"
                f"   {Emoji.MARKER} Правила игры - описание правил игры\n"
                f"   {Emoji.MARKER} О боте - техническая информация о боте (для разработчиков)\n"
                f"   {Emoji.MARKER} Новая игра - начать новую игру\n"
                f"2. Команды {Emoji.COMMAND}\n"
                f"   {Emoji.MARKER} /start - перезапустить бота\n"
                f"   {Emoji.MARKER} /help - открыть информацию о навигации по боту (данная справка)\n"
                f"   {Emoji.MARKER} /test - test\n\n\n"
                f"<b>Игра</b> {Emoji.GAME}\n"
                f"1. Кнопки {Emoji.BUTTON}\n"
                f"   {Emoji.MARKER} Выйти из игры - принудительно закончить игру\n"
                f"   {Emoji.MARKER} Скрыть меню - убрать меню снизу\n"
                f"2. Команды {Emoji.COMMAND}\n"
                f"   {Emoji.MARKER} /start - перезапустить бота\n"
                f"   {Emoji.MARKER} /menu - показать меню внизу экрана\n"
                f"   {Emoji.MARKER} /test - test\n\n"
            )
        },
        'reply': {
            'new_game': f"Выбери сложность игры {Emoji.HAND_DOWN}",
            'rules': (
                f"<b>Правила игры</b> {Emoji.BOOK}\n\n"
                f"В зависимости от выбранной сложности (<i>легко, средне, сложно</i>), <b>я загадаю число</b> в определенном диапазоне {Emoji.NUMBERS}\n\n"
                f"<b>Твоя задача - отгадать</b> это число за ограниченное количество попыток {Emoji.QUESTION_MARK}\n\n"
                f"Желаю удачи! {Emoji.COOL_FACE}"
            ),
            'about': '<a href="https://github.com/gle6chik/guess_the_number_bot_aiogram">Ссылка на репозиторий GitHub</a>'
        },
        'text': {
            'text': 'Чтобы сыграть, нажми "Новая игра"\nЧтобы посмотреть все действия, напиши /help'
        }
    },
    'game': {
        'command': {
            'change_menu': 'Меню открыто\nПродолжаем игру'
        },
        'reply': {
            'end_game': 'Игра окончена',
            'hide_menu': 'Меню скрыто\nПродолжаем игру'
        },
        'text': {
            'text_only': f"{Emoji.EXCLAMATION_MARK} Здесь нужно писать только числа"
        },
        'logic': {
            'win': lambda current_attempt, attempts, secret_num: (
                f"Победа! На {current_attempt} попытке из {attempts}! Ты молодец! {Emoji.LIKE}\nЗагаданное число - {secret_num}"
            ),
            'lose': lambda secret_num: (
                f"Количество попыток закончилось... {Emoji.SAD_FACE}\nЗагаданное число - {secret_num}\nНе переживай, в следующий раз повезёт! {Emoji.HUNDRED}"
            ),
            'more': lambda number, attempts_left: (
                f"Загаданное число БОЛЬШЕ {number}\nПопыток осталось: {attempts_left}"
            ),
            'less': lambda number, attempts_left: (
                f"Загаданное число МЕНЬШЕ {number}\nПопыток осталось: {attempts_left}"
            ),
            'start_game': lambda difficulty, attempts, range_num: (
                f"Режим сложности: {difficulty}\n"
                f"У тебя есть <b>{attempts} попыток</b>\n"
                f"Я загадал число в диапазоне <b>от 1 до {range_num}</b>, попробуй угадать! {Emoji.WINK}"
            )
        }
    }
}
