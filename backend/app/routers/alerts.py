from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.alert_service import get_factory_alerts

router = APIRouter(
    prefix="/api/v1/alerts",
    tags=["Alerts"]
)


@router.get("/")
def alerts(db: Session = Depends(get_db)):
    return get_factory_alerts(db)