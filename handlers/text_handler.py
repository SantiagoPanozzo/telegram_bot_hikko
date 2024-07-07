from telegram import Update
from telegram.ext import ContextTypes
from handlers.base_handler import BaseHandler

from commands.clima_command import ClimaCommand
from commands.contar_command import ContarCommand
from services import gemini_service


class TextHandler(BaseHandler):
    @staticmethod
    async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        text = update.message.text
        if text == "¡Quiero contar!":
            await ContarCommand.command(update, context)
        else:
            prompt = (
                        "Eres un bot de telegram. Tienes 2 funcionalidades principales: un contador, que aumenta en 1 "
                        "cada vez que lo utiliza un usuario; y una consulta de clima, que permite consultar el clima "
                        "en la zona en la que se encuentra el usuario. Cuando el usuario utiliza el comando del "
                        "clima, se enviará su ubicación actual y se mostrará el clima de todas las ciudades cercanas "
                        "a sus coordenadas. El comando del clima mostrará para cada ciudad cercana el nombre de la "
                        "ciudad, la temperatura, el estado del clima y la sensación térmica. El comando del clima no "
                        "está disponible en la aplicación de escritorio de Telegram ya que no se puede compartir la "
                        "ubicación. El usuario puede hacer uso de los comandos haciendo click en el botón de menú que "
                        "se encuentra a la derecha del cuadro de texto para enviar mensajes. El usuario acaba de "
                        "enviar un mensaje que no corresponde con ninguno de los comandos, por favor responde a su "
                        "mensaje de manera educada respondiendo cualquier pregunta que tenga el usuario y evita "
                        "confrontaciones. No debes simular el funcionamiento de los comandos, solo responder dudas e "
                        "indicarle al usuario como utilizar el bot. El mensaje enviado por el usuario es el siguiente:"
                        + text)
            response = await gemini_service.generate_content(prompt)
            await update.message.reply_markdown(response)
