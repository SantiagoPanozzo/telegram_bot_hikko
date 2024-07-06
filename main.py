from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler
from telegram.ext import filters

from utils.load_vars import env_vars
from utils.log import setup_logger

from commands.clima_command import ClimaCommand
from commands.start_command import StartCommand
from commands.contar_command import ContarCommand
from commands.coordenadas_command import CoordenadasCommand

from handlers.button_handler import ButtonHandler


def main() -> None:
    setup_logger()
    application = Application.builder().token(env_vars["TOKEN"]).build()
    application.add_handler(CommandHandler("start", StartCommand.command))
    application.add_handler(CommandHandler("contar", ContarCommand.command))
    application.add_handler(CommandHandler("coordenadas", CoordenadasCommand.command))
    application.add_handler(CommandHandler("clima", ClimaCommand.command))
    application.add_handler(CallbackQueryHandler(ButtonHandler.handle))
    application.run_polling()


if __name__ == "__main__":
    main()
