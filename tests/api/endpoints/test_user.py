import pytest
from api.crud.user import create_user, get_user, update_user, delete_user
from api.models.user import UserCreate


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
async def test_get_user(client, setup_teardown):
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "email@email.com",
        "join_date": "2023-01-01",
    }
    create_user(UserCreate(**user_data))
    response = await client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["name"] == "Test"
    assert response.json()["surname"] == "User"
    assert response.json()["height"] == 80
    assert response.json()["email"] == user_data["email"]
    assert response.json()["join_date"] == "2023-01-01"


@pytest.mark.anyio
async def test_update_user(client, setup_teardown):
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "email@email.com",
        "join_date": "2023-01-01",
    }
    create_user(UserCreate(**user_data))
    response = await client.put("/users/testuser", json={"name": "UpdatedName"})
    assert response.status_code == 200
    assert response.json()["nickname"] == "testuser"
    assert response.json()["name"] == "UpdatedName"


@pytest.mark.anyio
async def test_delete_user(client, setup_teardown):
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "email@email.com",
        "join_date": "2023-01-01",
    }
    create_user(UserCreate(**user_data))
    response = await client.delete("/users/testuser")
    assert response.status_code == 200
    assert response.json() == 1
