import pytest
from api.models import activity, base, health, user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope="module")
def database():
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/test")
    Session = sessionmaker(bind=engine)
    session = Session()

    base.Base.metadata.create_all(engine)
    
    yield session