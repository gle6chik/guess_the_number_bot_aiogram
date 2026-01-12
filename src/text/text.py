# constatns
MARKER_CODE = '\u2022'

MESSAGE = {
    'menu': {
        'callback': {
            'back': 'Нажми "Новая игра", чтобы сыграть!'
        },
        'command': {
            'start': (
                'Привет! Это игра <b>"Угадай число"</b>\n'
                'Готов проверить свою интуицию?'
            ),
            'help': (
                '<b>Навигация по боту</b>\n\n'
                'Есть два режима: <b>Меню</b> и <b>Игра</b>\n'
                'Ты можешь воспользоваться кнопками и командами\n\n'
                '<b>Меню</b>\n'
                '1. Кнопки\n'
                f"   {MARKER_CODE} Правила игры - описание правил игры\n"
                f"   {MARKER_CODE} О боте - техническая информация о боте (для разработчиков)\n"
                f"   {MARKER_CODE} Новая игра - начать новую игру\n"
                '2. Команды\n'
                f"   {MARKER_CODE} /start - перезапустить бота\n"
                f"   {MARKER_CODE} /help - открыть информацию о навигации по боту (данная справка)\n"
                f"   {MARKER_CODE} /test - test\n\n"
                '<b>Игра</b>\n'
                '1. Кнопки\n'
                f"   {MARKER_CODE} Выйти из игры - принудительно закончить игру\n"
                f"   {MARKER_CODE} Скрыть меню - убрать меню снизу\n\n"
                '2. Команды\n'
                f"   {MARKER_CODE} /start - перезапустить бота\n"
                f"   {MARKER_CODE} /menu - показать меню внизу экрана\n"
                f"   {MARKER_CODE} /test - test\n\n"
            )
        },
        'reply': {
            'new_game': 'Выбери сложность игры',
            'rules': (
                '<b>Правила игры</b>\n\n'
                'В зависимости от выбранной сложности (<i>легко, средне, сложно</i>), <b>я загадаю число</b> в определенном диапазоне.\n\n'
                '<b>Твоя задача - отгадать</b> это число за ограниченное количество попыток.\n\n'
                'Желаю удачи!'
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
            'text_only': 'Здесь нужно писать только числа'
        },
        'logic': {
            'win': lambda current_attempt, attempts, secret_num: (
                f"Победа! На {current_attempt} попытке из {attempts}! Ты молодец! Загаданное число - {secret_num}"
            ),
            'lose': lambda secret_num: (
                f"Количество попыток закончилось...\nЗагаданное число - {secret_num}\nНе переживай, в следующий раз повезёт!"
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
                f"Я загадал число в диапазоне <b>от 1 до {range_num}</b>, попробуй угадать!"
            )
        }
    }
}
