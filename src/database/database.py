import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

class UserDB:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            self.cur = self.conn.cursor()
        except psycopg2.Error as e:
            print(f"> Connecting error: {e}")
            raise
    
    # Write active
    def write_active(self, user_id: int, username: str, first_name: str, last_name: str):
        self.cur.execute("""
INSERT INTO users (user_id, username, first_name, last_name, last_activity)
VALUES (%s, %s, %s, %s, NOW())
ON CONFLICT (user_id)
DO UPDATE SET
last_activity = NOW(),
username = EXCLUDED.username,
first_name = EXCLUDED.first_name,
last_name = EXCLUDED.last_name
""", (user_id, username, first_name, last_name))
        self.conn.commit()
    
    # Write statistic
    def write_statistic(self, difficulty: str, user_id: int, attempt_result: int):
        best_result = difficulty + '_best_result'
        games_played = difficulty + '_games_played'
        
        self.cur.execute(
            f"""
INSERT INTO user_statistics (user_id, {best_result}, {games_played})
VALUES (%s, %s, 1)
ON CONFLICT (user_id)
DO UPDATE SET
{best_result} = CASE
WHEN %s = 0 THEN user_statistics.{best_result}
WHEN user_statistics.{best_result} = 0 THEN %s
ELSE LEAST(user_statistics.{best_result}, %s)
END,
{games_played} = user_statistics.{games_played} + 1;
""", (user_id, attempt_result, attempt_result, attempt_result, attempt_result))
        self.conn.commit()
    
    # Read statistic
    def read_statistic(self, user_id: int):
        self.cur.execute(
            """
SELECT
easy_best_result,
medium_best_result,
hard_best_result,
easy_games_played,
medium_games_played,
hard_games_played,
total_games_played
FROM user_statistics
WHERE user_id = %s;
""", (user_id,))
        
        results = self.cur.fetchone()
        if results:
            return results[0], results[1], results[2], results[3], results[4], results[5], results[6]
        else:
            return (0, 0, 0, 0, 0, 0, 0)
    
    # Read top users
    def read_top_users(self):
        self.cur.execute(
            """
SELECT
CASE
WHEN u.username IS NOT NULL
THEN CONCAT('@', u.username)
ELSE u.first_name
END as name,
us.total_games_played
FROM users u
LEFT JOIN user_statistics us ON u.user_id = us.user_id
WHERE us.total_games_played > 0
ORDER BY total_games_played DESC
LIMIT 10;
""")
        
        results = self.cur.fetchall()
        return results
    
    # Clean statistics
    def delete_statistics(self, user_id: int):
        self.cur.execute("DELETE FROM user_statistics WHERE user_id = %s", (user_id,))
        self.conn.commit()

    # Close connection
    def close(self):
        self.cur.close()
        self.conn.close()

