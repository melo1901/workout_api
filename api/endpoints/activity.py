from fastapi.routing import APIRouter
from api.crud import activity as crud
from api.models.activity import ActivityCreate

router = APIRouter()

@router.post("", response_model=ActivityCreate)
async def create_activity(activity: ActivityCreate):
    return crud.create_activity(activity)