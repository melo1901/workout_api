import pytest
from api.crud.activity import (
    create_activity,
    get_activity,
    update_activity,
    delete_activity,
)
from api.models.user import UserCreate
from api.crud.user import create_user
from api.models.activity import ActivityCreate, ActivityUpdate
from api.models.activity import Activity


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
def test_create_activity(setup_teardown, test_create_user):
    activity_data = {
        "nickname": "testuser",
        "activity": "Running",
        "duration": "30 minutes",
        "kcal_burnt": 300,
        "date": "2023-01-01",
    }
    activity = ActivityCreate(**activity_data)
    return create_activity(activity)


def test_create_activity_(setup_teardown, test_create_activity):
    created_activity = test_create_activity
    assert created_activity.activity == "Running"


def test_get_activity(setup_teardown, test_create_activity):
    retrieved_activity = get_activity(test_create_activity.id)
    assert retrieved_activity.activity == "Running"


def test_update_activity(setup_teardown, test_create_activity):
    new_activity_data = ActivityUpdate(
        activity="Swimming", duration="45 minutes", kcal_burnt=400
    )
    updated_activity = update_activity(test_create_activity.id, new_activity_data)
    assert updated_activity.activity == "Swimming"


def test_delete_activity(setup_teardown, test_create_activity):
    result = delete_activity(test_create_activity.id)
    assert result == 1
