from sqlalchemy.orm import Session

from app.models.sensor import Sensor
from app.models.sensor_history import SensorHistory


def save_sensor(db: Session, sensor_data: dict):

    sensor = (
        db.query(Sensor)
        .filter(
            Sensor.machine_name == sensor_data["machine"]
        )
        .first()
    )

    if sensor:

        sensor.temperature = sensor_data["temperature"]
        sensor.pressure = sensor_data["pressure"]
        sensor.humidity = sensor_data["humidity"]
        sensor.vibration = sensor_data["vibration"]
        sensor.status = sensor_data["status"]

    else:

        sensor = Sensor(

            machine_name=sensor_data["machine"],

            temperature=sensor_data["temperature"],

            pressure=sensor_data["pressure"],

            humidity=sensor_data["humidity"],

            vibration=sensor_data["vibration"],

            status=sensor_data["status"]

        )

        db.add(sensor)

    history = SensorHistory(

        machine_name=sensor_data["machine"],

        temperature=sensor_data["temperature"],

        pressure=sensor_data["pressure"],

        humidity=sensor_data["humidity"],

        vibration=sensor_data["vibration"],

        status=sensor_data["status"]

    )

    db.add(history)

    db.commit()

    db.refresh(sensor)

    return sensor