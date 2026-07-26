from pydantic import BaseModel


class FactoryOverview(BaseModel):
    total_machines: int
    running: int
    idle: int
    maintenance: int
    fault: int
    average_temperature: float