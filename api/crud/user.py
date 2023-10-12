import os
from fastapi import HTTPException
from api.models.user import Users, UserCreate, UserUpdate, UserResponse
from sqlalchemy.exc import IntegrityError
from api.database import session

def create_user(user: UserCreate):
    new_user = Users(**user.model_dump())
    try:
        session.add(new_user)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="Integrity constraint violation")
    return new_user

def get_user(nickname: str) -> UserResponse:
    user = session.query(Users).filter_by(nickname=nickname).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
    

def update_user(nickname: str, new_user_data: UserUpdate) -> UserUpdate:
    user = session.query(Users).filter_by(nickname=nickname).first()
    if user:
        for key, value in new_user_data:
            setattr(user, key, value)
        session.commit()
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
def delete_user(nickname: str) -> int:
    user = session.query(Users).filter_by(nickname=nickname).first()
    if user:
        session.delete(user)
        session.commit()
        return 1
    return 0