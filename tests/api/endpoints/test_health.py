import pytest
from api.crud.health import create_health
from api.crud.user import create_user
from api.models.health import HealthCreate
from httpx import AsyncClient
from api.models.user import UserCreate


@pytest.fixture
def create_health_fixture():
    health_data = {
        "nickname": "testuser",
        "blood_pressure": "120/80",
        "pulse": 80,
        "weight": 80,
    }
    return create_health(HealthCreate(**health_data))


@pytest.fixture
def create_user_fixture():
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "email@email.com",
        "join_date": "2023-01-01",
    }
    return create_user(UserCreate(**user_data))


@pytest.mark.anyio
async def test_create_health(client: AsyncClient, setup_teardown, create_user_fixture):
    await create_user_fixture
    health_data = {
        "nickname": "testuser",
        "blood_pressure": "120/80",
        "pulse": 80,
        "weight": 80,
    }
    response = await client.post("/health", json=health_data)
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["blood_pressure"] == "120/80"
    assert response.json()["pulse"] == 80
    assert response.json()["weight"] == 80


@pytest.mark.anyio
async def test_get_health(
    client: AsyncClient, setup_teardown, create_health_fixture, create_user_fixture
):
    await create_user_fixture
    await create_health_fixture
    response = await client.get("/health/1")
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["blood_pressure"] == "120/80"
    assert response.json()["pulse"] == 80
    assert response.json()["weight"] == 80


@pytest.mark.anyio
async def test_update_health(
    client: AsyncClient, setup_teardown, create_health_fixture, create_user_fixture
):
    await create_user_fixture
    await create_health_fixture
    health_data = {
        "nickname": "testuser",
        "blood_pressure": "120/90",
        "pulse": 83,
    }
    response = await client.put("/health/1", json=health_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["blood_pressure"] == "120/90"
    assert response.json()["pulse"] == 83
    assert response.json()["weight"] == 80


@pytest.mark.anyio
async def test_delete_health(
    client: AsyncClient, setup_teardown, create_health_fixture, create_user_fixture
):
    await create_user_fixture
    await create_health_fixture
    response = await client.delete("/health/1")
    assert response.status_code == 200
    assert response.json() == 1
