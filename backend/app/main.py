from fastapi import FastAPI

from app.database.init_db import init_db

from app.routers.machine import router as machine_router
from app.routers.sensor import router as sensor_router
from app.routers.analytics import router as analytics_router


# Create all database tables
init_db()


app = FastAPI(
    title="Smart Factory Digital Twin API",
    description="Industry 4.0 Smart Factory Backend using FastAPI, PostgreSQL, SQLAlchemy and MQTT",
    version="0.8.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Factory Digital Twin API",
        "version": "0.8.0",
        "status": "Running",
    }


# Register Routers
app.include_router(machine_router)
app.include_router(sensor_router)
app.include_router(analytics_router)