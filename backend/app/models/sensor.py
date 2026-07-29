from datetime import datetime

from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    machine_name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    temperature: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    pressure: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    humidity: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    vibration: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )