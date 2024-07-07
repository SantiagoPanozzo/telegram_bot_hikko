from telegram import Update
from telegram.ext import ContextTypes
from handlers.base_handler import BaseHandler

from commands.clima_command import ClimaCommand
from commands.contar_command import ContarCommand


class TextHandler(BaseHandler):
    @staticmethod
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        text = update.message.text
        if text == "¡Quiero contar!":
            await ContarCommand.command(update, context)
        else:
            await update.message.reply_text("Comando no válido.")
