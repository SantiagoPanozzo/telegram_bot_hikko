from telegram import Update
from telegram.ext import ContextTypes


class BaseCommand:
    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE):
        raise NotImplementedError("Falta implementar el código de ejecución del comando.")

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplementedError("Falta implementar el código del comando.")
