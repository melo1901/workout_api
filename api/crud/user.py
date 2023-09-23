from api.models.user import User
from api.database import session

def create_user(user):
    new_user = User(**user.model_dump())
    session.add(new_user)
    session.commit()
    return new_user