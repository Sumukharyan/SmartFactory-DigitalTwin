from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.machine import MachineCreate, MachineResponse

from app.services.machine_service import (
    get_all_machines,
    get_machine_by_id,
    create_machine,
    update_machine,
    delete_machine,
)

router = APIRouter(
    prefix="/api/v1/machines",
    tags=["Machines"],
)


@router.get("/", response_model=list[MachineResponse])
def read_all_machines(db: Session = Depends(get_db)):
    return get_all_machines(db)


@router.get("/{machine_id}", response_model=MachineResponse)
def read_machine(machine_id: int, db: Session = Depends(get_db)):
    machine = get_machine_by_id(db, machine_id)

    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")

    return machine


@router.post("/", response_model=MachineResponse)
def add_machine(machine: MachineCreate, db: Session = Depends(get_db)):
    return create_machine(db, machine)


@router.put("/{machine_id}", response_model=MachineResponse)
def edit_machine(
    machine_id: int,
    machine: MachineCreate,
    db: Session = Depends(get_db),
):
    updated = update_machine(db, machine_id, machine)

    if not updated:
        raise HTTPException(status_code=404, detail="Machine not found")

    return updated


@router.delete("/{machine_id}")
def remove_machine(machine_id: int, db: Session = Depends(get_db)):
    deleted = delete_machine(db, machine_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Machine not found")

    return {"message": "Machine deleted successfully"}