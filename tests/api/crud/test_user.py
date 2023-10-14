import pytest
from api.models.user import Users, UserCreate, UserUpdate
from api.crud.user import create_user, get_user, update_user, delete_user


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


@pytest.mark.anyio
async def test_create_user_(setup_teardown, test_create_user):
    created_user = await test_create_user
    assert created_user.nickname == "testuser"


@pytest.mark.anyio
async def test_get_user(setup_teardown, test_create_user):
    await test_create_user
    retrieved_user = await get_user("testuser")
    assert retrieved_user.nickname == "testuser"


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
async def test_delete_user(setup_teardown, test_create_user):
    await test_create_user
    result = await delete_user("testuser")
    assert result == 1
