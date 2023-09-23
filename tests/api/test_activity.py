from api.crud.activity import create_activity, get_activity, update_activity, delete_activity

def test_create_activity(database):
    activity_data = {
        "nickname": "test",
        "activity": "test2",
        "duration": "test2",
        "kcal_burnt": 2,
        "date": "2018-01-02",
    }

    created_activity = create_activity(activity_data, database)
    
    assert created_activity.id is not None
    assert created_activity.nickname == "test"
    assert created_activity.activity == "test2"
    assert created_activity.duration == "test2"
    assert created_activity.kcal_burnt == 2
    assert str(created_activity.date) == "2018-01-02"

def test_get_activity(database):
    activity_data = {
        "nickname": "test",
        "activity": "test2",
        "duration": "test2",
        "kcal_burnt": 2,
        "date": "2018-01-02",
    }

    created_activity = create_activity(activity_data, database)
    retrieved_activity = get_activity(created_activity.id, database)

    assert retrieved_activity is not None
    assert retrieved_activity.id == created_activity.id

def test_update_activity(database):
    activity_data = {
        "nickname": "test",
        "activity": "test2",
        "duration": "test2",
        "kcal_burnt": 2,
        "date": "2018-01-02",
    }

    created_activity = create_activity(activity_data, database)
    new_activity_data = {
        "activity": "updated_activity",
        "kcal_burnt": 5,
    }

    updated_activity = update_activity(created_activity.id, new_activity_data, database)

    assert updated_activity is not None
    assert updated_activity.activity == "updated_activity"
    assert updated_activity.kcal_burnt == 5

def test_delete_activity(database):
    activity_data = {
        "nickname": "test",
        "activity": "test2",
        "duration": "test2",
        "kcal_burnt": 2,
        "date": "2018-01-02",
    }

    created_activity = create_activity(activity_data, database)
    deleted_activity = delete_activity(created_activity.id, database)

    assert deleted_activity is not None
    assert deleted_activity.id == created_activity.id


    retrieved_activity = get_activity(created_activity.id, database)
    assert retrieved_activity is None
