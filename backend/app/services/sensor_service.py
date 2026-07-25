from sqlalchemy.orm import Session

from app.models.sensor import Sensor
from app.schemas.sensor import SensorCreate


def get_all_sensors(db: Session):
    return db.query(Sensor).all()


def get_sensor_by_id(db: Session, sensor_id: int):
    return db.query(Sensor).filter(Sensor.id == sensor_id).first()


def create_sensor(db: Session, sensor: SensorCreate):
    db_sensor = Sensor(
        type=sensor.type,
        value=sensor.value,
        unit=sensor.unit
    )

    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)

    return db_sensor


def update_sensor(
    db: Session,
    sensor_id: int,
    sensor: SensorCreate
):
    db_sensor = db.query(Sensor).filter(
        Sensor.id == sensor_id
    ).first()

    if db_sensor is None:
        return None

    db_sensor.type = sensor.type
    db_sensor.value = sensor.value
    db_sensor.unit = sensor.unit

    db.commit()
    db.refresh(db_sensor)

    return db_sensor


def delete_sensor(db: Session, sensor_id: int):
    db_sensor = db.query(Sensor).filter(
        Sensor.id == sensor_id
    ).first()

    if db_sensor is None:
        return False

    db.delete(db_sensor)
    db.commit()

    return True