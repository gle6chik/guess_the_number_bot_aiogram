#!/bin/bash

set -e

if [ $# -lt 3 ]; then
    echo -e "\e[31mОШИБКА: Все параметры обязательны.\e[0m"
    echo -e "Использование: $0 \e[1;91m<имя_бд>\e[0m \e[1;91m<пользователь>\e[0m \e[1;91m<пароль>\e[0m"
    echo -e "Пример: $0 \e[32mmy_db\e[0m \e[32mmy_user\e[0m \e[32mmy_very_hard_password\e[0m"
    exit 1
fi

DB_NAME=$1
DB_USER=$2
DB_PASS=$3

echo -e "\e[93mНастройка базы данных...\e[0m"
echo -e "\e[93mБаза данных:\e[0m $DB_NAME"
echo -e "\e[93mПользователь:\e[0m $DB_USER"

if ! pg_isready > /dev/null 2>&1; then
    echo -e "\e[31mОШИБКА: PostgreSQL не запущен\e[0m"
    exit 1
fi

sudo -u postgres psql << EOF

CREATE DATABASE $DB_NAME;
\c $DB_NAME
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';

GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
\i migrations/001_initial.sql

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO $DB_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO $DB_USER;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO $DB_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO $DB_USER;

GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO $DB_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT EXECUTE ON FUNCTIONS TO $DB_USER;

\q

EOF

echo -e "\e[32mУСПЕШНО:\e[0m создана база данных $DB_NAME"
echo -e "\e[32mУСПЕШНО:\e[0m создан пользователь $DB_USER\n"
echo -e "Проверить подключение: \e[36mpsql -h localhost -U $DB_USER -d $DB_NAME\e[0m\n"
echo -e "\e[93mВ файл \e[1;33m.env\e[0;93m вставлять эти данные:\e[0m"
echo "   DB_HOST=localhost"
echo "   DB_PORT=5432"
echo "   DB_NAME=$DB_NAME"
echo "   DB_USER=$DB_USER"
echo "   DB_PASSWORD=$DB_PASS"
