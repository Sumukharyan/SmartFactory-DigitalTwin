from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from app.models.machine import Machine
from app.models.sensor import Sensor
from app.models.sensor_history import SensorHistory


# ==================================================
# Health Score Calculator
# ==================================================

def calculate_health(sensor, status):

    score = 100

    score -= max(0, sensor.temperature - 30) * 1.5

    score -= abs(sensor.pressure - 100) * 0.7

    score -= max(0, sensor.humidity - 60) * 0.4

    score -= sensor.vibration * 4

    if status == "Idle":
        score -= 5

    elif status == "Maintenance":
        score -= 20

    elif status == "Fault":
        score -= 40

    score = max(0, min(100, round(score)))

    return score


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

    avg_temp = db.query(func.avg(Sensor.temperature)).scalar() or 0

    sensors = db.query(Sensor).all()

    scores = []

    for sensor in sensors:
        scores.append(
            calculate_health(sensor, sensor.status)
        )

    avg_health = (
        round(sum(scores) / len(scores), 1)
        if scores
        else 0
    )

    return {
        "total_machines": total,
        "running": running,
        "idle": idle,
        "maintenance": maintenance,
        "fault": fault,
        "average_temperature": round(avg_temp, 2),
        "average_health": avg_health,
    }


# ==================================================
# Sensor Summary
# ==================================================

def get_sensor_summary(db: Session):

    avg_temp = db.query(func.avg(Sensor.temperature)).scalar() or 0
    min_temp = db.query(func.min(Sensor.temperature)).scalar() or 0
    max_temp = db.query(func.max(Sensor.temperature)).scalar() or 0

    avg_pressure = db.query(func.avg(Sensor.pressure)).scalar() or 0
    min_pressure = db.query(func.min(Sensor.pressure)).scalar() or 0
    max_pressure = db.query(func.max(Sensor.pressure)).scalar() or 0

    avg_humidity = db.query(func.avg(Sensor.humidity)).scalar() or 0
    min_humidity = db.query(func.min(Sensor.humidity)).scalar() or 0
    max_humidity = db.query(func.max(Sensor.humidity)).scalar() or 0

    avg_vibration = db.query(func.avg(Sensor.vibration)).scalar() or 0
    min_vibration = db.query(func.min(Sensor.vibration)).scalar() or 0
    max_vibration = db.query(func.max(Sensor.vibration)).scalar() or 0

    return {
        "temperature": {
            "average": round(avg_temp, 2),
            "minimum": round(min_temp, 2),
            "maximum": round(max_temp, 2),
        },
        "pressure": {
            "average": round(avg_pressure, 2),
            "minimum": round(min_pressure, 2),
            "maximum": round(max_pressure, 2),
        },
        "humidity": {
            "average": round(avg_humidity, 2),
            "minimum": round(min_humidity, 2),
            "maximum": round(max_humidity, 2),
        },
        "vibration": {
            "average": round(avg_vibration, 2),
            "minimum": round(min_vibration, 2),
            "maximum": round(max_vibration, 2),
        },
    }


# ==================================================
# Machine Health
# ==================================================

def get_machine_health(db: Session):

    machines = db.query(Machine).all()

    health = []

    for machine in machines:

        sensor = (
            db.query(Sensor)
            .filter(Sensor.machine_name == machine.name)
            .first()
        )

        if not sensor:
            continue

        health_score = calculate_health(sensor, machine.status)

        if health_score >= 95:
            condition = "Excellent"
        elif health_score >= 80:
            condition = "Healthy"
        elif health_score >= 60:
            condition = "Warning"
        else:
            condition = "Critical"

        health.append(
            {
                "id": machine.id,
                "name": machine.name,
                "status": machine.status,
                "condition": condition,
                "health_score": health_score,
                "temperature": sensor.temperature,
                "pressure": sensor.pressure,
                "humidity": sensor.humidity,
                "vibration": sensor.vibration,
                "updated_at": sensor.updated_at.strftime("%H:%M:%S")
                if sensor.updated_at
                else "--",
            }
        )

    return health


# ==================================================
# Live Factory Status
# ==================================================

def get_live_factory_status(db: Session):

    latest = (
        db.query(Sensor)
        .order_by(Sensor.updated_at.desc())
        .first()
    )

    if not latest:
        return {
            "temperature": 0,
            "pressure": 0,
            "humidity": 0,
            "vibration": 0,
        }

    return {
        "temperature": latest.temperature,
        "pressure": latest.pressure,
        "humidity": latest.humidity,
        "vibration": latest.vibration,
    }


# ==================================================
# Sensor History
# ==================================================

def get_sensor_history(db: Session, limit: int = 30):

    history = (
        db.query(SensorHistory)
        .order_by(desc(SensorHistory.created_at))
        .limit(limit)
        .all()
    )

    history.reverse()

    return [
        {
            "time": row.created_at.strftime("%H:%M:%S"),
            "machine": row.machine_name,
            "temperature": row.temperature,
            "pressure": row.pressure,
            "humidity": row.humidity,
            "vibration": row.vibration,
            "status": row.status,
        }
        for row in history
    ]


# ==================================================
# Machine History
# ==================================================

def get_machine_history(
    db: Session,
    machine_name: str,
    limit: int = 20,
):

    history = (
        db.query(SensorHistory)
        .filter(
            SensorHistory.machine_name == machine_name
        )
        .order_by(
            SensorHistory.created_at.desc()
        )
        .limit(limit)
        .all()
    )

    history.reverse()

    return [
        {
            "time": row.created_at.strftime("%H:%M:%S"),
            "temperature": row.temperature,
            "pressure": row.pressure,
            "humidity": row.humidity,
            "vibration": row.vibration,
            "status": row.status,
        }
        for row in history
    ]