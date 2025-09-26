import os
from dotenv import load_dotenv
from typing import Final

load_dotenv()

BOT_TOKEN: Final[str] = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("(BOT_TOKEN) не найден в переменных окружения")

API_KEY: Final[str] = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("(API_KEY) не найден в переменных окружения")

BASE_URL: Final[str] = os.getenv("BASE_URL")
if not BASE_URL:
    raise RuntimeError("(BASE_URL) не найден в переменных окружения")

SYSTEM_MESSAGE = {
    "role": "system",
    "content": ("Ты - полезный ассистент. "
                "Отвечай на вопросы информативно и понятно, предоставляя достаточно деталей для полного понимания темы."
                "Старайся быть лаконичным, избегая излишней воды и повторений." 
                "Перед отправкой ответа убедись в его точности, полноте и логичности."
                )
    }