from api.models.health import Health

def create_health(health, session):
    new_health = Health(**health)
    session.add(new_health)
    session.commit()
    return new_health

def get_health(health_id, session):
    return session.query(Health).filter_by(id=health_id).first()

def update_health(health_id, new_health_data, session):
    health = session.query(Health).filter_by(id=health_id).first()
    if health:
        for key, value in new_health_data.items():
            setattr(health, key, value)
        session.commit()
    return health

def delete_health(health_id, session):
    health = session.query(Health).filter_by(id=health_id).first()
    if health:
        session.delete(health)
        session.commit()
    return health