import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apscheduler.schedulers.blocking import BlockingScheduler
from bot.database.database import UserDB

def action():
    db = UserDB()
    db.daily_task()
    db.close()

scheduler = BlockingScheduler()
scheduler.add_job(action, 'interval', minutes=1)

scheduler.start()
