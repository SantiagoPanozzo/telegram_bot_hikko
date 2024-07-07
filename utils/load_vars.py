import os

from dotenv import load_dotenv

load_dotenv()

env_vars = {
    "TOKEN": os.getenv("TOKEN"),
    "WEATHER_API_KEY": os.getenv("WEATHER_API_KEY"),
    "API_KEY": os.getenv("API_KEY")
}