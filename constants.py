import os
from typing import cast
from dotenv import load_dotenv

load_dotenv()

DB_FOLDER = os.getenv("DB_FOLDER", "db")
CONTENT_FOLDER = os.getenv("CONTENT_FOLDER", "content")
URLS_FILENAME = os.getenv("URLS_FILENAME", "urls.txt")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
TEMPERATURE = cast(float, os.getenv("OPENAI_TEMPERATURE", 0.0))
ANSWER_LANGUAGE = os.getenv("ANSWER_LANGUAGE", "English")

CONTENT_FILE_TYPES = ["txt", "pdf"]