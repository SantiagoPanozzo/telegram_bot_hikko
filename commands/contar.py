from telegram import User, Update
from telegram.ext import ContextTypes
from services.contador_service import ContadorService

contador = ContadorService()


async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    count = await contador.count_up(user)
    await update.message.reply_text(f"Has enviado {count} mensajes.")
