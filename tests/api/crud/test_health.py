import pytest
from api.crud.health import create_health, get_health, update_health, delete_health
from api.models.health import HealthCreate, HealthUpdate
from api.models.user import UserCreate
from api.crud.user import create_user
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
        "date": "2023-01-01",
    }
    health = HealthCreate(**health_data)
    return create_health(health)


@pytest.mark.anyio
async def test_create_health_(setup_teardown, test_create_health, test_create_user):
    await test_create_user
    created_health = await test_create_health
    assert created_health.nickname == "testuser"


@pytest.mark.anyio
async def test_create_health_wrong_user(setup_teardown, test_create_user):
    await test_create_user
    health_data = {
        "nickname": "testuser2",
        "blood_pressure": "120/80",
        "pulse": 70,
        "weight": 70.5,
        "date": "2023-01-01",
    }
    health = HealthCreate(**health_data)
    try:
        await create_health(health)
    except HTTPException as e:
        assert e.status_code == 409
        assert e.detail == "Integrity constraint violation"


@pytest.mark.anyio
async def test_create_health_wrong_data(setup_teardown, test_create_user):
    await test_create_user
    health_data = {
        "nickname": "testuser2",
        "blood_pressure": "120/80",
        "pulse": "70",
        "weight": 70.5,
        "date": "2023-01-01",
    }
    health = HealthCreate(**health_data)
    try:
        await create_health(health)
    except HTTPException as e:
        assert e.status_code == 409
        assert e.detail == "Integrity constraint violation"


@pytest.mark.anyio
async def test_get_health(setup_teardown, test_create_health, test_create_user):
    await test_create_user
    health = await test_create_health
    retrieved_health = await get_health(health.id)
    assert retrieved_health.nickname == "testuser"


@pytest.mark.anyio
async def test_get_health_wrong_id(
    setup_teardown, test_create_health, test_create_user
):
    await test_create_user
    health = await test_create_health
    try:
        await get_health(health.id + 1)
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Health record not found"


@pytest.mark.anyio
async def test_update_health(setup_teardown, test_create_health, test_create_user):
    await test_create_user
    health = await test_create_health
    new_health_data = HealthUpdate(blood_pressure="130/85", pulse=75)
    updated_health = await update_health(health.id, new_health_data)
    assert updated_health.blood_pressure == "130/85"
    assert updated_health.pulse == 75
    assert updated_health.weight == 70.5


@pytest.mark.anyio
async def test_update_health_wrong_id(
    setup_teardown, test_create_health, test_create_user
):
    await test_create_user
    health = await test_create_health
    new_health_data = HealthUpdate(blood_pressure="130/85", pulse=75)
    try:
        await update_health(health.id + 1, new_health_data)
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == "Health record not found"


@pytest.mark.anyio
async def test_delete_health(setup_teardown, test_create_health, test_create_user):
    await test_create_user
    health = await test_create_health
    result = await delete_health(health.id)
    assert result == 1


@pytest.mark.anyio
async def test_delete_health_wrong_id(
    setup_teardown, test_create_health, test_create_user
):
    await test_create_user
    health = await test_create_health
    result = await delete_health(health.id + 1)
    assert result == 0
