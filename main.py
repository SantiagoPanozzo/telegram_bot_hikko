import logging
import os

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from database.sqlite_connection import SqliteConnection

from commands.contador import Contador
from commands.clima import Clima

# Cargar variables de entorno (por ahora solo el token del bot)
load_dotenv()
TOKEN = os.getenv("TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
print(TOKEN)
print(WEATHER_API_KEY)


# Habilitar el logger, según la documentación de la API
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
connection = SqliteConnection()
connection.define_data()

contador: Contador = Contador(connection)
clima: Clima = Clima(connection, WEATHER_API_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hola {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Ayuda!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


async def contar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    count = await contador.count_up(user)
    await update.message.reply_text(f"Has enviado {count} mensajes.")


async def coords(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if len(context.args) == 0:
        lat, lon = await clima.get_coords(user)
        await update.message.reply_text(f"Tus coordenadas son: {lat}, {lon}")
    elif len(context.args) == 2:
        lat, lon = context.args
        await clima.set_coords(float(lat), float(lon), user)
        await update.message.reply_text("Coordenadas guardadas.")
    else:
        await update.message.reply_text("Sintaxis: /coordenadas o /coordenadas <latitud> <longitud>")


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    response = await clima.get_weather(user)
    await update.message.reply_text(response.json())


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler("contar", contar))
    application.add_handler(CommandHandler("coordenadas", coords))
    application.add_handler(CommandHandler("clima", weather))

    application.run_polling()


if __name__ == "__main__":
    main()
