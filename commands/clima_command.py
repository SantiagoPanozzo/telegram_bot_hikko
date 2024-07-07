from telegram import Update, error
from telegram.ext import ContextTypes

from commands.base_command import BaseCommand
from commands.start_command import StartCommand
from services.clima_service import get_weather
from database.sqlite_connection import SqliteConnection

from utils.load_vars import env_vars


class ClimaCommand(BaseCommand):
    @staticmethod
    async def execute(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        return await get_weather(user, pretty=True)

    @staticmethod
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        response = await ClimaCommand.execute(update, context)
        await update.message.reply_markdown(response, reply_markup=StartCommand.menu)

