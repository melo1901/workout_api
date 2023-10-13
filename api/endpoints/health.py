from fastapi.routing import APIRouter
from api.crud import health as crud
from api.models.health import HealthCreate, HealthResponse

router = APIRouter()


@router.post("", response_model=HealthCreate)
async def create_health(health: HealthCreate) -> HealthCreate:
    return crud.create_health(health)


@router.get("/{health_id}", response_model=HealthResponse)
async def get_health(health_id: int) -> HealthCreate:
    return crud.get_health(health_id)


@router.put("/{health_id}", response_model=HealthCreate)
async def update_health(health_id: int, new_health_data: HealthCreate) -> HealthCreate:
    return crud.update_health(health_id, new_health_data)


@router.delete("/{health_id}")
async def delete_health(health_id: int) -> int:
    return crud.delete_health(health_id)
