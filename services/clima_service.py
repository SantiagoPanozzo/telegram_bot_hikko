import requests

from database.sqlite_connection import SqliteConnection
from telegram import User
from utils.load_vars import env_vars


url = 'https://api.openweathermap.org/data/2.5/find?'
db = SqliteConnection()
api_key = env_vars["WEATHER_API_KEY"]


def query(lat: float, lon: float):
    return requests.get(f'{url}&appid={api_key}&lat={lat}&lon={lon}&units=metric').json()


def get_pretty_weather(lat: float, lon: float):
    respuesta = []

    data = query(lat, lon)
    regiones = data['list']

    for region in regiones:
        nombre_region = str(region['name']).upper()
        clima = str(region['weather'][0]['description']).capitalize()
        temp = region['main']['temp']
        term = region['main']['feels_like']
        respuesta.append(f"*{nombre_region}*\n" +
                         f"Clima: `{clima}`\n" +
                         f"Temperatura: `{temp}°C`\n" +
                         f"Sensación Térmica: `{term}°C`\n")

    return str.join("\n", respuesta)


async def set_coords(lat: float, lon: float, user: User):
    db.execute(f"INSERT OR IGNORE INTO user (user_id) VALUES ({user.id})")
    db.execute(f"UPDATE user SET latitude = {lat}, longitude = {lon} WHERE user_id = {user.id}")


async def get_coords(user: User):
    return db.fetchone(f"SELECT latitude, longitude FROM user WHERE user_id = {user.id}")


async def get_weather(user: User, pretty: bool = False) -> str:
    lat, lon = await get_coords(user)
    if pretty:
        return get_pretty_weather(lat, lon)
    return query(lat, lon)
