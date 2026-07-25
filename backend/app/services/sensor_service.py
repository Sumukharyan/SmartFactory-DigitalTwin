from sqlalchemy.orm import Session

from app.models.sensor import Sensor


def get_all_sensors(db: Session):
    return db.query(Sensor).all()


def create_sensor(db: Session, sensor: Sensor):
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return sensor