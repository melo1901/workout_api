import pytest
from typing import Generator, AsyncGenerator
from api.models import base
from sqlalchemy.orm import Session
from api.database import session as session_db
from api.database import engine as engine_db
from httpx import AsyncClient


@pytest.fixture(scope="function")
def setup_teardown() -> Generator[Session, None, None]:
    engine = engine_db
    base.Base.metadata.create_all(engine)
    session = session_db

    yield session

    session.rollback()
    session.close()
    base.Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, None]:
    from api.main import app

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"
