from api.models.health import Health, HealthCreate, HealthUpdate
from api.database import session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def create_health(health: HealthCreate):
    new_health = Health(**health.model_dump())
    try:
        session.add(new_health)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="Integrity constraint violation")
    return new_health


def get_health(health_id: int):
    health = session.query(Health).filter_by(id=health_id).first()
    if health:
        return health
    raise HTTPException(status_code=404, detail="Health record not found")


def update_health(health_id: int, new_health_data: HealthUpdate):
    health = session.query(Health).filter_by(id=health_id).first()
    if health:
        for key, value in new_health_data.model_dump(exclude_unset=True).items():
            setattr(health, key, value)
        session.commit()
    return health


def delete_health(health_id: int):
    health = session.query(Health).filter_by(id=health_id).first()
    if health:
        session.delete(health)
        session.commit()
        return 1
    return 0
