from fastapi import APIRouter
from app.schemas.sensor import Sensor

router = APIRouter()

sensors = [
    Sensor(
        id=1,
        type="Temperature",
        value=28.5,
        unit="°C"
    ),
    Sensor(
        id=2,
        type="Vibration",
        value=1.6,
        unit="mm/s"
    )
]

@router.get("/sensors", response_model=list[Sensor])
def get_sensors():
    return sensors