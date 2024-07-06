from telegram import Update
from telegram.ext import ContextTypes


class BaseHandler:
    @staticmethod
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplementedError("Falta implementar el código del handler.")

