from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    type: Mapped[str] = mapped_column(String(50), nullable=False)

    value: Mapped[float] = mapped_column(Float, nullable=False)

    unit: Mapped[str] = mapped_column(String(20), nullable=False)