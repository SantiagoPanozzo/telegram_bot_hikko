from commands.base_command import BaseCommand
from telegram import Update
from telegram.ext import ContextTypes
from services.location_service import set_coords


class LocationCommand(BaseCommand):
    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        location = update.message.location
        await set_coords(location.latitude, location.longitude, user)
        return "Coordenadas guardadas."

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = await LocationCommand.execute(update, context)
        await update.message.reply_text(response)

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = await LocationCommand.execute(update, context)
        await update.callback_query.edit_message_text(response)
