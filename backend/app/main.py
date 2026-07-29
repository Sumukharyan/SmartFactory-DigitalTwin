from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import machine
from app.routers import sensor
from app.routers import analytics
from app.routers import alerts

app = FastAPI(
    title="Smart Factory Digital Twin API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(machine.router)
app.include_router(sensor.router)
app.include_router(analytics.router)
app.include_router(alerts.router)


@app.get("/")
def root():
    return {"message": "Smart Factory API Running 🚀"}