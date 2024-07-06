from telegram import Update
from telegram.ext import ContextTypes

from commands.base_command import BaseCommand
from commands.start_command import StartCommand
from services.clima_service import get_coords, set_coords
from utils.load_vars import env_vars


class CoordenadasCommand(BaseCommand):
    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
        user = update.effective_user
        if context.args is None or len(context.args) == 0:
            lat, lon = await get_coords(user)
            return f"Tus coordenadas son: {lat}, {lon}. Escribe `/coordenadas <latitud> <longitud> para cambiarlas.`"
        elif len(context.args) == 2:
            lat, lon = context.args
            await set_coords(float(lat), float(lon), user)
            return "Coordenadas guardadas."
        else:
            return "Sintaxis: `/coordenadas` o `/coordenadas <latitud> <longitud>`"

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = await CoordenadasCommand.execute(update, context)
        await update.message.reply_markdown(response, reply_markup=StartCommand.menu)

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = await CoordenadasCommand.execute(update, context)
        await update.callback_query.edit_message_text(response, reply_markup=StartCommand.menu)
