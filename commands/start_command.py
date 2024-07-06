from telegram import ForceReply, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from commands.base_command import BaseCommand


class StartCommand(BaseCommand):
    menu: InlineKeyboardMarkup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("¡Quiero saber el clima!", callback_data="clima"),
                InlineKeyboardButton("¡Quiero contar!", callback_data="contar")
            ],
            [InlineKeyboardButton("¡Quiero ver mis coordenadas!", callback_data="coordenadas")],
        ]
    )

    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> InlineKeyboardMarkup:
        user = update.effective_user
        return StartCommand.menu

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Elige una opción:", reply_markup=await StartCommand.execute(update, context))

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer("Opción no válida.")
