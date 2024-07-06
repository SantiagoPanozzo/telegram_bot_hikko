from database.sqlite_connection import SqliteConnection
from telegram import User


db = SqliteConnection()


async def count_up(user: User):
    db.execute(f"INSERT OR IGNORE INTO user (user_id) VALUES ({user.id})")
    db.execute(f"UPDATE user SET count = count + 1 WHERE user_id = {user.id}")
    return db.fetchone(f"SELECT count FROM user WHERE user_id = {user.id}")[0]
