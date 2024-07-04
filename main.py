import logging
import os
import utils.load_vars

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from database.sqlite_connection import SqliteConnection

from commands import start, contar, coordenadas, clima

from utils.load_vars import env_vars

# Habilitar el logger, según la documentación de la API
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def main() -> None:
    application = Application.builder().token(env_vars["TOKEN"]).build()
    application.add_handler(CommandHandler("start", start.command))
    application.add_handler(CommandHandler("contar", contar.command))
    application.add_handler(CommandHandler("coordenadas", coordenadas.command))
    application.add_handler(CommandHandler("clima", clima.command))

    application.run_polling()


if __name__ == "__main__":
    main()
