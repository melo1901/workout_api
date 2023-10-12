from json import JSONDecodeError
from fastapi import HTTPException
from fastapi.routing import APIRouter
from api.crud import user as crud
from api.models.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.post("", response_model=(UserCreate | None))
async def create_user(activity: UserCreate) -> UserCreate | None:
    return crud.create_user(activity)


@router.get("/{nickname}", response_model=(UserResponse))
async def get_user(nickname: str) -> UserResponse:
    return crud.get_user(nickname)


@router.put("/{nickname}", response_model=UserUpdate)
async def update_user(nickname: str, user: UserUpdate) -> UserUpdate:
    return crud.update_user(nickname, user)


@router.delete("/{nickname}", response_model=int)
async def delete_user(nickname: str) -> int:
    return crud.delete_user(nickname)
