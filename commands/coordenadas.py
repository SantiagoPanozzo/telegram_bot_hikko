from telegram import Update
from telegram.ext import ContextTypes

from services.clima_service import ClimaService
from database.sqlite_connection import SqliteConnection
from utils.load_vars import env_vars

connection = SqliteConnection()

clima = ClimaService(connection, env_vars["WEATHER_API_KEY"])


async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if len(context.args) == 0:
        lat, lon = await clima.get_coords(user)
        await update.message.reply_text(f"Tus coordenadas son: {lat}, {lon}")
    elif len(context.args) == 2:
        lat, lon = context.args
        await clima.set_coords(float(lat), float(lon), user)
        await update.message.reply_text("Coordenadas guardadas.")
    else:
        await update.message.reply_text("Sintaxis: /coordenadas o /coordenadas <latitud> <longitud>")
