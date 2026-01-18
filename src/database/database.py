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
            print('> Connected to database.')
        except psycopg2.Error as e:
            print(f"> Connecting error: {e}")
            raise
    
    # Write
    def write(self, user_id: int, username: str, first_name: str, last_name: str):
        self.cur.execute(
            "INSERT INTO users (user_id, username, first_name, last_name, last_activity)"
            "VALUES (%s, %s, %s, %s, NOW())"
            "ON CONFLICT (user_id)"
            "DO UPDATE SET"
            "   last_activity = NOW(),"
            "   username = EXCLUDED.username,"
            "   first_name = EXCLUDED.first_name,"
            "   last_name = EXCLUDED.last_name",
            (user_id, username, first_name, last_name))
        
        print(f"> Information was written.")
        self.conn.commit()
    
    # Close connection
    def close(self):
        self.cur.close()
        self.conn.close()
        print('Connection closed.')

