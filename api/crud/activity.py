from api.models.activity import Activity
from api.database import session

def create_activity(activity):
    new_activity = Activity(**activity.model_dump())
    session.add(new_activity)
    session.commit()
    return activity


def get_activity(activity_id, session):
    return session.query(Activity).filter_by(id=activity_id).first()


def update_activity(activity_id, new_activity_data, session):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        for key, value in new_activity_data.items():
            setattr(activity, key, value)
        session.commit()
    return activity

def delete_activity(activity_id, session):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        session.delete(activity)
        session.commit()
    return activity
