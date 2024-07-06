from telegram import Update
from telegram.ext import ContextTypes

from commands.clima_command import ClimaCommand
from commands.contar_command import ContarCommand
from commands.coordenadas_command import CoordenadasCommand
from handlers.base_handler import BaseHandler


class ButtonHandler(BaseHandler):
    @staticmethod
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        callback_data = update.callback_query.data
        if callback_data == "clima":
            await ClimaCommand.callback(update, context)
        elif callback_data == "contar":
            await ContarCommand.callback(update, context)
        elif callback_data == "coordenadas":
            await CoordenadasCommand.callback(update, context)
        else:
            await update.callback_query.answer("Opción no válida.")
