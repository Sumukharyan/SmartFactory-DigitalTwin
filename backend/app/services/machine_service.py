from sqlalchemy.orm import Session

from app.models.machine import Machine
from app.schemas.machine import MachineCreate


def get_all_machines(db: Session):
    return db.query(Machine).all()


def get_machine_by_id(db: Session, machine_id: int):
    return db.query(Machine).filter(Machine.id == machine_id).first()


def create_machine(db: Session, machine: MachineCreate):
    db_machine = Machine(
        name=machine.name,
        status=machine.status,
        temperature=machine.temperature
    )
def update_machine(
    db: Session,
    machine_id: int,
    machine: MachineCreate
):
    db_machine = db.query(Machine).filter(
        Machine.id == machine_id
    ).first()

    if db_machine is None:
        return None

    db_machine.name = machine.name
    db_machine.status = machine.status
    db_machine.temperature = machine.temperature

    db.commit()
    db.refresh(db_machine)

    return db_machine

def delete_machine(db: Session, machine_id: int):
    db_machine = (
        db.query(Machine)
        .filter(Machine.id == machine_id)
        .first()
    )

    if db_machine is None:
        return False

    db.delete(db_machine)
    db.commit()

    return True