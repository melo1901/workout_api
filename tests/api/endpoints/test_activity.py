import pytest
from api.crud.activity import create_activity
from api.crud.user import create_user
from api.models.activity import ActivityCreate
from httpx import AsyncClient
from api.models.user import UserCreate


@pytest.fixture
def create_activity_fixture():
    activity_data = {
        "nickname": "testuser",
        "activity": "Running",
        "duration": "00:30:00",
        "kcal_burned": 100,
        "date": "2023-01-01",
    }
    return create_activity(ActivityCreate(**activity_data))


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
async def test_create_activity(
    client: AsyncClient, setup_teardown, create_user_fixture
):
    await create_user_fixture
    activity_data = {
        "nickname": "testuser",
        "activity": "Running",
        "duration": "00:30:00",
        "kcal_burned": 100,
        "date": "2023-01-01",
    }
    response = await client.post("/activities", json=activity_data)
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["activity"] == "Running"
    assert response.json()["duration"] == "00:30:00"
    assert response.json()["kcal_burned"] == 100
    assert response.json()["date"] == "2023-01-01"


@pytest.mark.anyio
async def test_create_activity_wrong_data(client: AsyncClient, setup_teardown):
    activity_data = {
        "nickname": "testuser",
        "activity": "Running",
        "duration": "00:30:00",
        "kcal_burned": 100,
    }
    response = await client.post("/activities", json=activity_data)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_activities(
    client: AsyncClient, setup_teardown, create_activity_fixture, create_user_fixture
):
    await create_user_fixture
    await create_activity_fixture
    response = await client.get("/activities/user/testuser")
    assert response.status_code == 200
    assert response.json()[0]["nickname"] == "testuser"
    assert response.json()[0]["activity"] == "Running"
    assert response.json()[0]["duration"] == "00:30:00"
    assert response.json()[0]["kcal_burned"] == 100
    assert response.json()[0]["date"] == "2023-01-01"


@pytest.mark.anyio
async def test_update_activity(
    client: AsyncClient, setup_teardown, create_activity_fixture, create_user_fixture
):
    await create_user_fixture
    await create_activity_fixture
    response = await client.put("/activities/1", json={"activity": "Walking"})
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["activity"] == "Walking"


@pytest.mark.anyio
async def test_update_activity_wrong_data(
    client: AsyncClient, setup_teardown, create_activity_fixture, create_user_fixture
):
    await create_user_fixture
    await create_activity_fixture
    response = await client.put("/activities/2", json={"kcal_burned": "100"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


@pytest.mark.anyio
async def test_delete_activity(
    client: AsyncClient, setup_teardown, create_activity_fixture, create_user_fixture
):
    await create_user_fixture
    await create_activity_fixture
    response = await client.delete("/activities/1")
    assert response.status_code == 200
    assert response.json() == 1


@pytest.mark.anyio
async def test_delete_activity_wrong_data(
    client: AsyncClient, setup_teardown, create_activity_fixture, create_user_fixture
):
    await create_user_fixture
    await create_activity_fixture
    response = await client.delete("/activities/2")
    assert response.status_code == 200
    assert response.json() == 0
