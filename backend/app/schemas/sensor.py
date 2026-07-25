from pydantic import BaseModel


class SensorCreate(BaseModel):
    type: str
    value: float
    unit: str


class SensorResponse(SensorCreate):
    id: int

    model_config = {
        "from_attributes": True
    }