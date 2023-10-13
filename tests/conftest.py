import pytest
from api.models import base
from api.database import session as session_db
from api.database import engine as engine_db
from httpx import AsyncClient


@pytest.fixture(scope="function")
def setup_teardown():
    engine = engine_db
    base.Base.metadata.create_all(engine)
    session = session_db

    yield session

    session.rollback()
    session.close()
    base.Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
async def client():
    from api.main import app

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def anyio_backend():
    return "asyncio"
