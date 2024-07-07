from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import filters

from utils.load_vars import env_vars
from utils.log import setup_logger

from commands.start_command import StartCommand

from handlers.text_handler import TextHandler
from handlers.location_handler import LocationHandler


def main() -> None:
    setup_logger()
    application = Application.builder().token(env_vars["TOKEN"]).build()
    application.add_handler(CommandHandler("start", StartCommand.command))
    application.add_handler(MessageHandler(filters.TEXT, TextHandler.handle))
    application.add_handler(MessageHandler(filters.LOCATION, LocationHandler.handle))
    application.run_polling()


if __name__ == "__main__":
    while True:
        main()
