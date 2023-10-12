import pytest
from api.models import base
from api.database import session as session_db
from api.database import engine as engine_db


@pytest.fixture(scope="function")
def setup_teardown():
    engine = engine_db
    base.Base.metadata.create_all(engine)
    session = session_db

    yield session

    session.rollback()
    session.close()
    base.Base.metadata.drop_all(engine)
