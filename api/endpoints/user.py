from fastapi.routing import APIRouter
from api.crud import user as crud
from api.models.user import UserCreate

router = APIRouter()

@router.post("", response_model=UserCreate)
async def create_user(activity: UserCreate):
    return crud.create_user(activity)