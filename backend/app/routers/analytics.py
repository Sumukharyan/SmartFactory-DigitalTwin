from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.analytics_service import (
    get_factory_overview,
    get_sensor_summary,
    get_machine_health,
    get_live_factory_status,
    get_sensor_history,
    get_machine_history,   
)

router = APIRouter(
    prefix="/api/v1/analytics",
    tags=["Analytics"],
)


@router.get("/overview")
def overview(db: Session = Depends(get_db)):
    return get_factory_overview(db)


@router.get("/sensor-summary")
def sensor_summary(db: Session = Depends(get_db)):
    return get_sensor_summary(db)


@router.get("/machine-health")
def machine_health(db: Session = Depends(get_db)):
    return get_machine_health(db)


@router.get("/live")
def live_status(db: Session = Depends(get_db)):
    return get_live_factory_status(db)


@router.get("/history/{machine_name}")
def machine_history(
    machine_name: str,
    db: Session = Depends(get_db)
):
    return get_machine_history(
        db,
        machine_name
    )

@router.get("/history")
def history(db: Session = Depends(get_db)):
    return get_sensor_history(db)

@router.get("/machine/{machine_name}")
def machine_history(machine_name: str):
    return analytics.get_machine_history(machine_name)