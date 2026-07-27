from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.init_db import init_db

from app.routers.machine import router as machine_router
from app.routers.sensor import router as sensor_router
from app.routers.analytics import router as analytics_router


# Create database tables
init_db()

app = FastAPI(
    title="Smart Factory Digital Twin API",
    description="Industry 4.0 Smart Factory Backend using FastAPI, PostgreSQL, SQLAlchemy and MQTT",
    version="0.9.0",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Factory Digital Twin API",
        "version": "0.9.0",
        "status": "Running",
    }


app.include_router(machine_router)
app.include_router(sensor_router)
app.include_router(analytics_router)