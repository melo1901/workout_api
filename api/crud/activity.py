from fastapi import HTTPException
from api.models.activity import Activity, ActivityCreate, ActivityUpdate
from api.models.user import Users
from api.database import session
from sqlalchemy.exc import IntegrityError


async def create_activity(activity: ActivityCreate):
    new_activity = Activity(**activity.model_dump())
    try:
        session.add(new_activity)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print(e)
        raise HTTPException(status_code=409, detail="Integrity constraint violation")
    return new_activity


async def get_activity(activity_id: int):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        return activity
    raise HTTPException(status_code=404, detail="Activity not found")


async def get_user_activities(user_nickname: str):
    user = session.query(Users).filter_by(nickname=user_nickname).all()

    if user:
        return session.query(Activity).filter_by(nickname=user_nickname).all()
    raise HTTPException(status_code=404, detail="User not found")


async def update_activity(activity_id: int, new_activity_data: ActivityUpdate):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        for key, value in new_activity_data.model_dump(exclude_unset=True).items():
            setattr(activity, key, value)
        session.commit()
        return activity
    raise HTTPException(status_code=404, detail="Activity not found")


async def delete_activity(activity_id: int):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        session.delete(activity)
        session.commit()
        return 1
    return 0
