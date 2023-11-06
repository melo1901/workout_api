from json import JSONDecodeError
from fastapi import HTTPException
from fastapi.routing import APIRouter
from api.crud import user as crud
from api.models.activity import ActivityResponse
from api.models.health import HealthResponse
from api.models.user import UserCreate, UserResponse, UserUpdate

router = APIRouter()


@router.post("", response_model=(UserCreate | None))
async def create_user(user: UserCreate) -> UserCreate | None:
    return await crud.create_user(user)


@router.get("/{nickname}", response_model=(UserResponse))
async def get_user(nickname: str) -> UserResponse:
    return await crud.get_user(nickname)


@router.put("/{nickname}", response_model=UserUpdate)
async def update_user(nickname: str, user: UserUpdate) -> UserUpdate:
    return await crud.update_user(nickname, user)


@router.delete("/{nickname}", response_model=int)
async def delete_user(nickname: str) -> int:
    return await crud.delete_user(nickname)


@router.get("", response_model=list[UserResponse])
async def get_users() -> list[UserResponse]:
    return await crud.get_users()


@router.get("/{nickname}/health", response_model=list[HealthResponse])
async def get_user_health_history(nickname: str) -> list[HealthResponse]:
    return await crud.get_user_health_history(nickname)


@router.get("/{nickname}/activities", response_model=list[ActivityResponse])
async def get_user_activities(nickname: str) -> list[ActivityResponse]:
    return await crud.get_user_activities(nickname)
