from sqlalchemy.orm import Session

from app.models.sensor import Sensor


def save_sensor(
    db: Session,
    sensor_type: str,
    value: float,
    unit: str,
):
    sensor = Sensor(
        type=sensor_type,
        value=value,
        unit=unit,
    )

    db.add(sensor)

    db.commit()

    db.refresh(sensor)

    return sensor