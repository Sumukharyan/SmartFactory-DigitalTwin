from sqlalchemy.orm import Session

from app.models.sensor import Sensor


def save_temperature(db: Session, temperature: float):
    sensor = Sensor(
        type="Temperature",
        value=temperature,
        unit="°C"
    )

    db.add(sensor)
    db.commit()
    db.refresh(sensor)

    return sensor