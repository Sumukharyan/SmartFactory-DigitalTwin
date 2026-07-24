from fastapi import APIRouter

from app.api.v1.endpoints import health, machines, sensors

api_router = APIRouter()

api_router.include_router(
    health.router,
    tags=["Health"]
)

api_router.include_router(
    machines.router,
    tags=["Machines"]
)

api_router.include_router(
    sensors.router,
    tags=["Sensors"]
)