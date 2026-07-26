from sqlalchemy.orm import Session

from app.models.machine import Machine


# ==========================
# CRUD FUNCTIONS
# ==========================

def get_all_machines(db: Session):
    return db.query(Machine).all()


def get_machine_by_id(db: Session, machine_id: int):
    return (
        db.query(Machine)
        .filter(Machine.id == machine_id)
        .first()
    )


def create_machine(db: Session, machine):
    new_machine = Machine(
        name=machine.name,
        status=machine.status,
        temperature=machine.temperature,
    )

    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)

    return new_machine


def update_machine(db: Session, machine_id: int, machine_data):
    machine = get_machine_by_id(db, machine_id)

    if not machine:
        return None

    machine.name = machine_data.name
    machine.status = machine_data.status
    machine.temperature = machine_data.temperature

    db.commit()
    db.refresh(machine)

    return machine


def delete_machine(db: Session, machine_id: int):
    machine = get_machine_by_id(db, machine_id)

    if not machine:
        return None

    db.delete(machine)
    db.commit()

    return machine


# ==========================
# MQTT FUNCTION
# ==========================

def update_machine_status(
    db: Session,
    machine_name: str,
    status: str,
):

    machine = (
        db.query(Machine)
        .filter(Machine.name == machine_name)
        .first()
    )

    if machine:

        machine.status = status

        db.commit()

        db.refresh(machine)

        return machine

    machine = Machine(
        name=machine_name,
        status=status,
        temperature=0.0,
    )

    db.add(machine)

    db.commit()

    db.refresh(machine)

    return machine