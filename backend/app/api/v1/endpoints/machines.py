from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.machine import MachineResponse
from app.services.machine_service import get_all_machines

router = APIRouter()


@router.get("/", response_model=list[MachineResponse])
def read_machines(db: Session = Depends(get_db)):
    return get_all_machines(db)