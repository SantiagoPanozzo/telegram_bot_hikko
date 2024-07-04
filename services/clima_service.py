import requests

from database.sqlite_connection import SqliteConnection
from telegram import User


class ClimaService:
    def __init__(self, db: SqliteConnection, api_key: str):
        self.url = 'https://api.openweathermap.org/data/2.5/find?'
        self.db = db
        self.api_key = api_key

    def query(self, lat: float, lon: float):
        return requests.get(f'{self.url}&appid={self.api_key}&lat={lat}&lon={lon}')

    async def set_coords(self, lat: float, lon: float, user: User):
        self.db.execute(f"INSERT OR IGNORE INTO user (user_id) VALUES ({user.id})")
        self.db.execute(f"UPDATE user SET latitude = {lat}, longitude = {lon} WHERE user_id = {user.id}")

    async def get_coords(self, user: User):
        return self.db.fetchone(f"SELECT latitude, longitude FROM user WHERE user_id = {user.id}")

    async def get_weather(self, user: User):
        lat, lon = await self.get_coords(user)
        return self.query(lat, lon)