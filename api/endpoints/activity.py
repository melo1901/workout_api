from fastapi.routing import APIRouter
from api.crud import activity as crud
from api.models.activity import ActivityCreate, ActivityResponse

router = APIRouter()

@router.post("", response_model=ActivityCreate)
async def create_activity(activity: ActivityCreate) -> ActivityCreate:
    return crud.create_activity(activity)

@router.get("/{activity_id}", response_model=ActivityResponse)
async def get_activity(activity_id: int) -> ActivityCreate:
    return crud.get_activity(activity_id)

@router.get("/user/{user_nickname}", response_model=list[ActivityResponse])
async def get_user_activities(user_nickname: str) -> list[ActivityResponse]:
    return crud.get_user_activities(user_nickname)

@router.put("/{activity_id}", response_model=ActivityCreate)
async def update_activity(activity_id: int, new_activity_data: ActivityCreate) -> ActivityCreate:
    return crud.update_activity(activity_id, new_activity_data)

@router.delete("/{activity_id}")
async def delete_activity(activity_id: int) -> int:
    return crud.delete_activity(activity_id)