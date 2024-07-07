from telegram import ForceReply, Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from commands.base_command import BaseCommand


class StartCommand(BaseCommand):

    menu: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        [
            [KeyboardButton("¡Quiero saber el clima!", request_location=True)],
            [KeyboardButton("¡Quiero contar!")]
        ]
    )

    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> ReplyKeyboardMarkup:
        user = update.effective_user
        return StartCommand.menu

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            text="Elige una opción:",
            reply_markup=await StartCommand.execute(update, context)
        )
