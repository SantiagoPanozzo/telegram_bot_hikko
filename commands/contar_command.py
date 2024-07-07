from telegram import User, Update, error
from telegram.ext import ContextTypes

from commands.base_command import BaseCommand
from services.contador_service import count_up
from commands.start_command import StartCommand


class ContarCommand(BaseCommand):
    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        user: User = update.effective_user
        return await count_up(user)

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        count = await ContarCommand.execute(update, context)
        await update.message.reply_text(
            text=f"Has enviado {count} mensajes.",
            reply_markup=StartCommand.menu
        )
