BEGIN;

-- Функция для автообновления updated_at в user_statistics
CREATE OR REPLACE FUNCTION auto_update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_activity TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Таблица статистики для пользователей
CREATE TABLE IF NOT EXISTS user_statistics (
    user_id BIGINT PRIMARY KEY,
    easy_games_played INTEGER DEFAULT 0,
    medium_games_played INTEGER DEFAULT 0,
    hard_games_played INTEGER DEFAULT 0,
    total_games_played INTEGER GENERATED ALWAYS AS (
        easy_games_played + medium_games_played + hard_games_played
    ) STORED,
    easy_best_result SMALLINT DEFAULT 0,
    medium_best_result SMALLINT DEFAULT 0,
    hard_best_result SMALLINT DEFAULT 0,
    games_won INTEGER DEFAULT 0,
    games_lost INTEGER DEFAULT 0,
    winning_percentage NUMERIC(5,2) GENERATED ALWAYS AS (
        CASE 
            WHEN (easy_games_played + medium_games_played + hard_games_played) > 0 
            THEN (games_won * 100)::NUMERIC / (easy_games_played + medium_games_played + hard_games_played)::NUMERIC
            ELSE 100.00
        END
    ) STORED,
    losing_percentage NUMERIC(5,2) GENERATED ALWAYS AS (
        CASE 
            WHEN (easy_games_played + medium_games_played + hard_games_played) > 0 
            THEN (games_lost * 100)::NUMERIC / (easy_games_played + medium_games_played + hard_games_played)::NUMERIC
            ELSE 100.00
        END
    ) STORED,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT user_statistics_user_id_fkey 
        FOREIGN KEY (user_id) 
        REFERENCES users(user_id) 
        ON DELETE CASCADE,
    CONSTRAINT easy_best_result_check CHECK (easy_best_result >= 0),
    CONSTRAINT medium_best_result_check CHECK (medium_best_result >= 0),
    CONSTRAINT hard_best_result_check CHECK (hard_best_result >= 0)
);

-- Удаление триггера, если он существует
DROP TRIGGER IF EXISTS update_user_statistics_timestamp ON user_statistics;
-- Триггер для автообновления updated_at в user_statistics
CREATE TRIGGER update_user_statistics_timestamp
    BEFORE UPDATE ON user_statistics
    FOR EACH ROW
    EXECUTE FUNCTION auto_update_timestamp();

COMMIT;

DO $$
BEGIN
    RAISE NOTICE 'Миграция применена: %', now();
END $$;

