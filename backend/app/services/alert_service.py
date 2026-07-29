from sqlalchemy.orm import Session

from app.models.sensor import Sensor


def get_factory_alerts(db: Session):

    alerts = []

    sensors = db.query(Sensor).all()

    for sensor in sensors:

        if sensor.status == "Fault":

            alerts.append({
                "level": "Critical",
                "message": f"{sensor.machine_name} has entered FAULT state."
            })

        if sensor.temperature > 40:

            alerts.append({
                "level": "Warning",
                "message": f"{sensor.machine_name} temperature is high ({sensor.temperature:.1f} °C)."
            })

        if sensor.vibration > 5:

            alerts.append({
                "level": "Warning",
                "message": f"{sensor.machine_name} vibration is high ({sensor.vibration:.1f} mm/s)."
            })

    return alerts