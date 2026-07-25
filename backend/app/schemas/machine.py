from pydantic import BaseModel


class MachineCreate(BaseModel):
    name: str
    status: str
    temperature: float


class MachineResponse(MachineCreate):
    id: int

    model_config = {
        "from_attributes": True
    }