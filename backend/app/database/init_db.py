from app.database.base import Base
from app.database.session import engine

from app.models.machine import Machine
from app.models.sensor import Sensor


def init_db():
    Base.metadata.create_all(bind=engine)