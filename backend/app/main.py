from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

@app.on_event("startup")
def startup():

    logger.info("Application Started")

@app.get("/")
def home():

    return {
        "message": "Welcome to Smart Factory Digital Twin API"
    }