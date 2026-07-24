from fastapi import APIRouter
from app.schemas.machine import Machine

router = APIRouter()

machines = [
    Machine(
        id=1,
        name="CNC Machine",
        status="Running",
        temperature=63.5
    ),
    Machine(
        id=2,
        name="Assembly Robot",
        status="Idle",
        temperature=39.1
    )
]

@router.get("/machines", response_model=list[Machine])
def get_machines():
    return machines