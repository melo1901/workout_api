import pytest
from api.crud.activity import (
    create_activity,
    get_activity,
    get_user_activities,
    update_activity,
    delete_activity,
)
from api.models.user import UserCreate
from api.crud.user import create_user
from api.models.activity import ActivityCreate, ActivityUpdate
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
    assert created_activity.nickname == "testuser"
    assert created_activity.activity == "Running"
    assert created_activity.duration == "00:30:00"
    assert created_activity.kcal_burned == 300
    assert created_activity.date == "2023-01-01"


@pytest.mark.anyio
async def test_create_activity_wrong_user(setup_teardown, test_create_user):
    await test_create_user
    activity_data = {
        "nickname": "testuser2",
        "activity": "Running",
        "duration": "00:30:00",
        "kcal_burned": 300,
        "date": "2023-01-01",
    }
    activity = ActivityCreate(**activity_data)
    try:
        await create_activity(activity)
    except HTTPException as e:
        assert e.detail == "Integrity constraint violation"


@pytest.mark.anyio
async def test_create_activity_wrong_data(setup_teardown, test_create_user):
    await test_create_user
    activity_data = {
        "nickname": "testuser2",
        "activity": "Running",
        "duration": "00:30:00",
        "kcal_burned": "300",
        "date": "2023-01-01",
    }
    activity = ActivityCreate(**activity_data)
    try:
        await create_activity(activity)
    except HTTPException as e:
        assert e.detail == "Integrity constraint violation"


@pytest.mark.anyio
async def test_get_activity(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    retrieved_activity = await get_activity(created_activity.id)
    assert retrieved_activity.nickname == "testuser"
    assert retrieved_activity.activity == "Running"
    assert retrieved_activity.duration == "00:30:00"
    assert retrieved_activity.kcal_burned == 300
    assert retrieved_activity.date == "2023-01-01"


@pytest.mark.anyio
async def test_get_activity_wrong_id(setup_teardown, test_create_user):
    await test_create_user
    try:
        await get_activity(2)
    except HTTPException as e:
        assert e.detail == "Activity not found"


@pytest.mark.anyio
async def test_get_user_activities(
    setup_teardown, test_create_activity, test_create_user
):
    await test_create_user
    created_activity = await test_create_activity
    retrieved_activity = await get_user_activities(created_activity.nickname)
    assert retrieved_activity[0].nickname == "testuser"
    assert retrieved_activity[0].activity == "Running"
    assert retrieved_activity[0].duration == "00:30:00"
    assert retrieved_activity[0].kcal_burned == 300
    assert retrieved_activity[0].date == "2023-01-01"


@pytest.mark.anyio
async def test_get_user_activities_empty(setup_teardown, test_create_user):
    await test_create_user
    retrieved_activity = await get_user_activities("testuser")
    assert retrieved_activity == []


@pytest.mark.anyio
async def test_update_activity(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    new_activity_data = ActivityUpdate(
        activity="Swimming", duration="00:45:00", kcal_burned=400
    )
    updated_activity = await update_activity(created_activity.id, new_activity_data)
    assert updated_activity.nickname == "testuser"
    assert updated_activity.activity == "Swimming"
    assert updated_activity.duration == "00:45:00"
    assert updated_activity.kcal_burned == 400
    assert updated_activity.date == "2023-01-01"


@pytest.mark.anyio
async def test_update_activity_wrong_id(setup_teardown, test_create_user):
    await test_create_user
    new_activity_data = ActivityUpdate(
        activity="Swimming", duration="00:45:00", kcal_burned=400
    )
    try:
        await update_activity(2, new_activity_data)
    except HTTPException as e:
        assert e.detail == "Activity not found"


@pytest.mark.anyio
async def test_delete_activity(setup_teardown, test_create_activity, test_create_user):
    await test_create_user
    created_activity = await test_create_activity
    result = await delete_activity(created_activity.id)
    assert result == 1


@pytest.mark.anyio
async def test_delete_activity_wrong_id(setup_teardown, test_create_user):
    await test_create_user
    result = await delete_activity(2)
    assert result == 0
