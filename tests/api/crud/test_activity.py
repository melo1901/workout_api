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
    return create_user(user)


@pytest.fixture
async def test_create_activity(setup_teardown, test_create_user):
    activity_data = {
        "nickname": "testuser",
        "activity": "Running",
        "duration": "00:30:00",
        "kcal_burned": 300,
        "date": "2023-01-01",
    }
    activity = ActivityCreate(**activity_data)
    return create_activity(activity)


@pytest.mark.anyio
async def test_create_activity_(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    assert created_activity.activity == "Running"


@pytest.mark.anyio
async def test_get_activity(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    retrieved_activity = await get_activity(created_activity.id)
    assert retrieved_activity.activity == "Running"


@pytest.mark.anyio
async def test_update_activity(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    new_activity_data = ActivityUpdate(
        activity="Swimming", duration="00:45:00", kcal_burned=400
    )
    updated_activity = await update_activity(created_activity.id, new_activity_data)
    assert updated_activity.activity == "Swimming"


@pytest.mark.anyio
async def test_delete_activity(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    result = await delete_activity(created_activity.id)
    assert result == 1
