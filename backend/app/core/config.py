from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    VERSION = os.getenv("VERSION")
    DEBUG = os.getenv("DEBUG") == "True"
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()