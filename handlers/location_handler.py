from telegram import Update
from telegram.ext import ContextTypes
from handlers.base_handler import BaseHandler
from services.location_service import set_coords

from commands.clima_command import ClimaCommand
from commands.contar_command import ContarCommand


class LocationHandler(BaseHandler):
    @staticmethod
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user = update.effective_user
        location = update.message.location
        await set_coords(location.latitude, location.longitude, user)
        await ClimaCommand.command(update, context)
