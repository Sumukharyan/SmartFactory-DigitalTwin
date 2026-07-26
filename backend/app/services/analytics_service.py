from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.machine import Machine
from app.models.sensor import Sensor


# ==================================================
# Factory Overview
# ==================================================

def get_factory_overview(db: Session):

    total = db.query(Machine).count()

    running = (
        db.query(Machine)
        .filter(Machine.status == "Running")
        .count()
    )

    idle = (
        db.query(Machine)
        .filter(Machine.status == "Idle")
        .count()
    )

    maintenance = (
        db.query(Machine)
        .filter(Machine.status == "Maintenance")
        .count()
    )

    fault = (
        db.query(Machine)
        .filter(Machine.status == "Fault")
        .count()
    )

    avg_temp = (
        db.query(func.avg(Sensor.value))
        .filter(Sensor.type == "Temperature")
        .scalar()
    )

    if avg_temp is None:
        avg_temp = 0

    return {
        "total_machines": total,
        "running": running,
        "idle": idle,
        "maintenance": maintenance,
        "fault": fault,
        "average_temperature": round(avg_temp, 2),
    }


# ==================================================
# Sensor Summary
# ==================================================

def get_sensor_summary(db: Session):

    sensor_types = [
        "Temperature",
        "Pressure",
        "Humidity",
        "Vibration",
    ]

    summary = {}

    for sensor in sensor_types:

        average = (
            db.query(func.avg(Sensor.value))
            .filter(Sensor.type == sensor)
            .scalar()
        )

        minimum = (
            db.query(func.min(Sensor.value))
            .filter(Sensor.type == sensor)
            .scalar()
        )

        maximum = (
            db.query(func.max(Sensor.value))
            .filter(Sensor.type == sensor)
            .scalar()
        )

        summary[sensor.lower()] = {
            "average": round(average or 0, 2),
            "minimum": round(minimum or 0, 2),
            "maximum": round(maximum or 0, 2),
        }

    return summary


# ==================================================
# Machine Health
# ==================================================

def get_machine_health(db: Session):

    machines = db.query(Machine).all()

    health = []

    for machine in machines:

        if machine.status == "Running":
            condition = "Healthy"

        elif machine.status == "Idle":
            condition = "Standby"

        elif machine.status == "Maintenance":
            condition = "Needs Maintenance"

        else:
            condition = "Critical"

        health.append(
            {
                "id": machine.id,
                "name": machine.name,
                "status": machine.status,
                "condition": condition,
            }
        )

    return health


# ==================================================
# Live Factory Status
# ==================================================

def get_live_factory_status(db: Session):

    latest_temperature = (
        db.query(Sensor)
        .filter(Sensor.type == "Temperature")
        .order_by(Sensor.id.desc())
        .first()
    )

    latest_pressure = (
        db.query(Sensor)
        .filter(Sensor.type == "Pressure")
        .order_by(Sensor.id.desc())
        .first()
    )

    latest_humidity = (
        db.query(Sensor)
        .filter(Sensor.type == "Humidity")
        .order_by(Sensor.id.desc())
        .first()
    )

    latest_vibration = (
        db.query(Sensor)
        .filter(Sensor.type == "Vibration")
        .order_by(Sensor.id.desc())
        .first()
    )

    return {
        "temperature": latest_temperature.value if latest_temperature else None,
        "pressure": latest_pressure.value if latest_pressure else None,
        "humidity": latest_humidity.value if latest_humidity else None,
        "vibration": latest_vibration.value if latest_vibration else None,
    }