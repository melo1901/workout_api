import pytest
from api.crud.health import create_health, get_health, update_health, delete_health
from api.models.health import HealthCreate, HealthUpdate
from api.models.user import UserCreate
from api.crud.user import create_user


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
    create_user(user)


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


def test_create_health_(setup_teardown, test_create_health):
    created_health = test_create_health
    assert created_health.nickname == "testuser"


def test_get_health(setup_teardown, test_create_health):
    retrieved_health = get_health(test_create_health.id)
    assert retrieved_health.nickname == "testuser"


def test_update_health(setup_teardown, test_create_health):
    new_health_data = HealthUpdate(blood_pressure="130/85", pulse=75)
    updated_health = update_health(test_create_health.id, new_health_data)
    assert updated_health.blood_pressure == "130/85"
    assert updated_health.pulse == 75
    assert updated_health.weight == 70.5


def test_delete_health(setup_teardown, test_create_health):
    result = delete_health(test_create_health.id)
    assert result == 1
