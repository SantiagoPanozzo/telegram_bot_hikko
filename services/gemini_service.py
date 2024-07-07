import google.generativeai as genai
import os

from utils.load_vars import env_vars


genai.configure(api_key=env_vars["API_KEY"])


async def generate_content(text: str) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = await model.generate_content_async(text)
    return response.text
