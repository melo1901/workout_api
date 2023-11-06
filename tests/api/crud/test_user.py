import pytest
from api.crud.health import create_health
from api.models.health import HealthCreate
from api.models.user import Users, UserCreate, UserUpdate
from api.crud.user import (
    create_user,
    get_user,
    get_user_health_history,
    get_users,
    update_user,
    delete_user,
)
from fastapi import HTTPException


@pytest.fixture
def test_create_user():
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "test@example.com",
        "join_date": "2023-01-01",
    }
    user = UserCreate(**user_data)
    return create_user(user)


@pytest.fixture
def test_create_health(setup_teardown, test_create_user):
    health_data = {
        "nickname": "testuser",
        "blood_pressure": "120/80",
        "pulse": 70,
        "weight": 70.5,
    }
    health = HealthCreate(**health_data)
    return create_health(health)


@pytest.mark.anyio
async def test_create_user_(setup_teardown, test_create_user):
    created_user = await test_create_user
    assert created_user.nickname == "testuser"


@pytest.mark.anyio
async def test_create_user_duplicate(setup_teardown, test_create_user):
    await test_create_user
    user_data = {
        "nickname": "testuser",
        "name": "Test",
        "surname": "User",
        "height": 80,
        "email": "test@example.com",
        "join_date": "2023-01-01",
    }
    user = UserCreate(**user_data)
    try:
        await create_user(user)
    except HTTPException as e:
        assert e.status_code == 409
        assert e.detail == "Integrity constraint violation"


@pytest.mark.anyio
async def test_get_user(setup_teardown, test_create_user):
    await test_create_user
    retrieved_user = await get_user("testuser")
    assert retrieved_user.nickname == "testuser"


@pytest.mark.anyio
async def test_get_user_not_found(setup_teardown, test_create_user):
    await test_create_user
    try:
        await get_user("testuser2")
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "User not found"


@pytest.mark.anyio
async def test_update_user(setup_teardown, test_create_user):
    await test_create_user

    new_user_data = UserUpdate(
        name="UpdatedName", surname="UpdatedSurname", email="updated@example.com"
    )
    updated_user = await update_user("testuser", new_user_data)
    assert updated_user.name == "UpdatedName"
    assert updated_user.surname == "UpdatedSurname"
    assert updated_user.email == "updated@example.com"


@pytest.mark.anyio
async def test_update_user_not_found(setup_teardown, test_create_user):
    await test_create_user

    new_user_data = UserUpdate(
        name="UpdatedName", surname="UpdatedSurname", email="updated@example.com"
    )
    try:
        await update_user("testuser", new_user_data)
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "User not found"


@pytest.mark.anyio
async def test_delete_user(setup_teardown, test_create_user):
    await test_create_user
    result = await delete_user("testuser")
    assert result == 1


@pytest.mark.anyio
async def test_delete_user_not_found(setup_teardown, test_create_user):
    await test_create_user
    result = await delete_user("testuser2")
    assert result == 0


@pytest.mark.anyio
async def test_get_users(setup_teardown, test_create_user):
    await test_create_user
    users = await get_users()
    assert len(users) == 1
    assert users[0].nickname == "testuser"


@pytest.mark.anyio
async def test_get_users_empty(setup_teardown):
    users = await get_users()
    assert users == []


@pytest.mark.anyio
async def test_get_user_health_history(
    setup_teardown, test_create_health, test_create_user
):
    await test_create_user
    health = await test_create_health
    retrieved_health = await get_user_health_history(health.nickname)
    assert retrieved_health[0].nickname == "testuser"
    assert retrieved_health[0].blood_pressure == "120/80"
    assert retrieved_health[0].pulse == 70
    assert retrieved_health[0].weight == 70.5


@pytest.mark.anyio
async def test_get_user_health_history_empty(setup_teardown, test_create_user):
    await test_create_user
    try:
        await get_user_health_history("testuser")
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "User not found"
