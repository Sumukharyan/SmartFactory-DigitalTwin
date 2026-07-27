from app.database.connection import engine
from app.database.base import Base

# Import models so SQLAlchemy knows about them
from app.models.machine import Machine
from app.models.sensor import Sensor
from app.models.sensor_history import SensorHistory

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")