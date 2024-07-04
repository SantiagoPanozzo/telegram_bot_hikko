from telegram import Update
from telegram.ext import ContextTypes

from services.clima_service import ClimaService
from database.sqlite_connection import SqliteConnection

from utils.load_vars import env_vars

clima = ClimaService(SqliteConnection(), env_vars["WEATHER_API_KEY"])


async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    response = await clima.get_weather(user)
    await update.message.reply_text(response.json())
