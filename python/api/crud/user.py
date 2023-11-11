import os
from fastapi import HTTPException
from api.models.activity import Activity
from api.models.health import Health
from api.models.user import Users, UserCreate, UserUpdate, UserResponse
from sqlalchemy.exc import IntegrityError
from api.database import session


async def create_user(user: UserCreate):
    new_user = Users(**user.model_dump())
    try:
        session.add(new_user)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="Integrity constraint violation")
    return new_user


async def get_user(nickname: str) -> UserResponse:
    user = session.query(Users).filter_by(nickname=nickname).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def update_user(nickname: str, new_user_data: UserUpdate) -> UserUpdate:
    user = session.query(Users).filter_by(nickname=nickname).first()
    if user:
        for key, value in new_user_data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        session.commit()
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def delete_user(nickname: str) -> int:
    user = session.query(Users).filter_by(nickname=nickname).first()
    if user:
        session.delete(user)
        session.commit()
        return 1
    return 0


async def get_users() -> list:
    return session.query(Users).all()


async def get_user_health_history(nickname: str) -> list:
    health_data = session.query(Health).filter_by(nickname=nickname).all()
    if health_data:
        return health_data
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def get_user_activities(user_nickname: str) -> list:
    user = session.query(Users).filter_by(nickname=user_nickname).all()
    if user:
        return session.query(Activity).filter_by(nickname=user_nickname).all()
    else:
        raise HTTPException(status_code=404, detail="User not found")
