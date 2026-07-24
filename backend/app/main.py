from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

@app.on_event("startup")
def startup():
    logger.info("Application Started")

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Factory Digital Twin API"
    }