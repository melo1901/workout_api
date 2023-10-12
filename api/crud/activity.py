from fastapi import HTTPException
from api.models.activity import Activity, ActivityCreate
from api.models.user import Users
from api.database import session
from sqlalchemy.exc import IntegrityError


def create_activity(activity: ActivityCreate):
    new_activity = Activity(**activity.model_dump())
    try:
        session.add(new_activity)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="Integrity constraint violation")
    return new_activity


def get_activity(activity_id: int):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        return activity
    raise HTTPException(status_code=404, detail="Activity not found")


def get_user_activities(user_nickname: str):
    user = session.query(Users).filter_by(nickname=user_nickname).first()

    if user:
        return user.activities
    raise HTTPException(status_code=404, detail="User not found")


def update_activity(activity_id: int, new_activity_data):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        for key, value in new_activity_data:
            setattr(activity, key, value)
        session.commit()
    return activity


def delete_activity(activity_id: int):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        session.delete(activity)
        session.commit()
        return 1
    return 0
