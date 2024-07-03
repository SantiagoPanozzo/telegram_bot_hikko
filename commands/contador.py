from telegram import User
from database.sqlite_connection import SqliteConnection


class Contador:
    def __init__(self, db: SqliteConnection = SqliteConnection()):
        self.db = db

    async def count_up(self, user: User):
        self.db.execute(f"INSERT OR IGNORE INTO user (user_id) VALUES ({user.id})")
        self.db.execute(f"UPDATE user SET count = count + 1 WHERE user_id = {user.id}")
        return self.db.fetchone(f"SELECT count FROM user WHERE user_id = {user.id}")[0]
