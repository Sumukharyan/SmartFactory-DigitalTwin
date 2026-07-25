from sqlalchemy.orm import Session

from app.models.machine import Machine


def get_all_machines(db: Session):
    return db.query(Machine).all()


def create_machine(db: Session, machine: Machine):
    db.add(machine)
    db.commit()
    db.refresh(machine)
    return machine