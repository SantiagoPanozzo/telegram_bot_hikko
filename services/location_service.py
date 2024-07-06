from telegram import User

from database.sqlite_connection import SqliteConnection

db = SqliteConnection()


async def set_coords(lat: float, lon: float, user: User):
    db.execute(f"INSERT OR IGNORE INTO user (user_id) VALUES ({user.id})")
    db.execute(f"UPDATE user SET latitude = {lat}, longitude = {lon} WHERE user_id = {user.id}")


async def get_coords(user: User):
    return db.fetchone(f"SELECT latitude, longitude FROM user WHERE user_id = {user.id}")
