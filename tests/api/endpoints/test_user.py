import pytest
from api.crud.health import create_health
from api.crud.user import create_user, get_user, update_user, delete_user
from api.models.health import HealthCreate
from api.models.user import UserCreate


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


@pytest.fixture
def create_health_fixture():
    health_data = {
        "nickname": "testuser",
        "blood_pressure": "120/80",
        "pulse": 70,
        "weight": 70.5,
        "date": "2023-01-01",
    }
    health = HealthCreate(**health_data)
    return create_health(health)


@pytest.mark.anyio
async def test_create_user(client, setup_teardown):
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "email@email.com",
        "join_date": "2023-01-01",
    }
    response = await client.post("/users", json=user_data)
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["name"] == "Test"
    assert response.json()["email"] == "email@email.com"


@pytest.mark.anyio
async def test_create_user_wrong_data(client, setup_teardown):
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "join_date": "2023-01-01",
    }
    response = await client.post("/users", json=user_data)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_user(client, setup_teardown, create_user_fixture):
    await create_user_fixture
    response = await client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["name"] == "Test"
    assert response.json()["surname"] == "User"
    assert response.json()["height"] == 80
    assert response.json()["email"] == "email@email.com"
    assert response.json()["join_date"] == "2023-01-01"


@pytest.mark.anyio
async def test_get_user_wrong_nickname(client, setup_teardown):
    response = await client.get("/users/testuser")
    assert response.status_code == 404


@pytest.mark.anyio
async def test_update_user(client, setup_teardown, create_user_fixture):
    await create_user_fixture
    response = await client.put("/users/testuser", json={"name": "UpdatedName"})
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["name"] == "UpdatedName"


@pytest.mark.anyio
async def test_update_user_wrong_nickname(client, setup_teardown):
    response = await client.put("/users/testuser", json={"name": "UpdatedName"})
    assert response.status_code == 404


@pytest.mark.anyio
async def test_delete_user(client, setup_teardown, create_user_fixture):
    await create_user_fixture
    response = await client.delete("/users/testuser")
    assert response.status_code == 200
    assert response.json() == 1


@pytest.mark.anyio
async def test_delete_user_wrong_nickname(client, setup_teardown):
    response = await client.delete("/users/testuser")
    assert response.status_code == 200
    assert response.json() == 0


@pytest.mark.anyio
async def test_get_users(client, setup_teardown, create_user_fixture):
    await create_user_fixture
    response = await client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["nickname"] == "testuser"
    assert response.json()[0]["name"] == "Test"


@pytest.mark.anyio
async def test_get_users_empty(client, setup_teardown):
    response = await client.get("/users")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_get_user_health_history(
    client, setup_teardown, create_user_fixture, create_health_fixture
):
    await create_user_fixture
    await create_health_fixture
    response = await client.get("/users/testuser/health")
    assert response.status_code == 200
    assert response.json()[0]["nickname"] == "testuser"


@pytest.mark.anyio
async def test_get_user_health_history_wrong_nickname(client, setup_teardown):
    response = await client.get("/users/testuser/health")
    assert response.status_code == 404
