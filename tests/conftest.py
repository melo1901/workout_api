import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models.base import Base
from api.models.activity import Activity
from api.models.health import Health
from api.models.user import User

@pytest.fixture(scope="session")
def database():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/test")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session