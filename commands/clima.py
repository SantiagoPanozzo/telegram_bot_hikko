from database.sqlite_connection import SqliteConnection
from telegram import User


class Clima:
    def __init__(self, db: SqliteConnection = SqliteConnection()):
        self.db = db

    async def set_coords(self, lat: float, lon: float, user: User):
        self.db.execute(f"INSERT OR IGNORE INTO user (user_id) VALUES ({user.id})")
        self.db.execute(f"UPDATE user SET latitude = {lat}, longitude = {lon} WHERE user_id = {user.id}")

    async def get_coords(self, user: User):
        return self.db.fetchone(f"SELECT latitude, longitude FROM user WHERE user_id = {user.id}")