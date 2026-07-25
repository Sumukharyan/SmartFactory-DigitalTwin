from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.sensor import SensorResponse
from app.services.sensor_service import get_all_sensors

router = APIRouter()


@router.get("/", response_model=list[SensorResponse])
def read_sensors(db: Session = Depends(get_db)):
    return get_all_sensors(db)