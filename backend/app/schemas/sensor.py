from pydantic import BaseModel

class Sensor(BaseModel):
    id: int
    type: str
    value: float
    unit: str