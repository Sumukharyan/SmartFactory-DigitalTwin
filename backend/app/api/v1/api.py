from fastapi import APIRouter

from app.api.v1.endpoints import health, machines, sensors

api_router = APIRouter()

api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

api_router.include_router(
    machines.router,
    prefix="/machines",
    tags=["Machines"]
)

api_router.include_router(
    sensors.router,
    prefix="/sensors",
    tags=["Sensors"]
)