# Chat bot de Telegram

## Descripción:
Bot creado como prueba técnica para Hikko. Dispone de los botones necesarios para el clima y el contador, y
una integración con Gemini para generación de texto en casos no contemplados.

## Detalles:
Existen 2 ramas. La rama principal tiene la versión del código más cómoda con las funcionalidades básicas.
La rama "version1" tiene código más viejo con distinta implementación del menú. Mantengo esta versión porque
es más compleja y con más comandos y funcionalidades, pero es menos intuitiva de utilizar, así que dejo la versión
más simple como principal.

## Funcionalidades:
- **Clima**
- **Contador**
- **IA**


## Set-Up:
### 0. Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:
```
TOKEN=TokenDeTelegram
WEATHER_API_KEY=KeyDeOpenWeatherMap
API_KEY=KeyDeGoogleAiStudio
```

### 1. Crear un entorno virtual:
```
python -m venv .venv
```

### 2. Instalar las dependencias:
```
./.venv/bin/pip install -r requirements.txt
```

### 3. Correr el bot:
```
./.venv/bin/python main.py
```