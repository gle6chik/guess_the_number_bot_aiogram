import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from bot.database.database import UserDB

app = FastAPI(title='Admin panel')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://127.0.0.1:3000'],
    # allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, etc.)
    allow_headers=["*"]  # Разрешить все заголовки
)

class User:
    def __init__(self,
                 user_id: int,
                 username: str,
                 first_name: str,
                 last_name: str,
                 created_at: str,
                 last_activity: str):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at
        self.last_activity = last_activity
        
# GET /
@app.get("/")
async def root():
    return 'It is root.'

# GET /users
@app.get("/users")
async def get_users():
    db = UserDB()
    data = db.get_all_users()
    db.close()
    result = []
    for row in data:
        result.append({
            'user_id': row[0],
            'username': row[1],
            'first_name': row[2],
            'last_name': row[3],
            'created_at': row[4],
            'last_activity': row[5]
        })
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8080)
