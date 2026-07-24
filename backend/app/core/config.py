from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    VERSION = os.getenv("VERSION")
    DEBUG = os.getenv("DEBUG")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))

settings = Settings()