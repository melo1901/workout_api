# from api.crud.health import create_health, get_health, update_health, delete_health

# def test_create_health(database):
#     health_data = {
#         "nickname": "test",
#         "blood_pressure": "120/80",
#         "pulse": 70,
#     }

#     created_health = create_health(health_data, database)

#     assert created_health.id is not None
#     assert created_health.nickname == "test"
#     assert created_health.blood_pressure == "120/80"
#     assert created_health.pulse == 70

# def test_get_health(database):
#     health_data = {
#         "nickname": "test",
#         "blood_pressure": "120/80",
#         "pulse": 70,
#     }

#     created_health = create_health(health_data, database)
#     retrieved_health = get_health(created_health.id, database)

#     assert retrieved_health is not None
#     assert retrieved_health.id == created_health.id

# def test_update_health(database):
#     health_data = {
#         "nickname": "test",
#         "blood_pressure": "120/80",
#         "pulse": 70,
#     }

#     created_health = create_health(health_data, database)
#     new_health_data = {
#         "blood_pressure": "130/85",
#         "pulse": 75,
#     }

#     updated_health = update_health(created_health.id, new_health_data, database)

#     assert updated_health is not None
#     assert updated_health.blood_pressure == "130/85"
#     assert updated_health.pulse == 75

# def test_delete_health(database):
#     health_data = {
#         "nickname": "test",
#         "blood_pressure": "120/80",
#         "pulse": 70,
#     }

#     created_health = create_health(health_data, database)
#     deleted_health = delete_health(created_health.id, database)

#     assert deleted_health is not None
#     assert deleted_health.id == created_health.id

#     retrieved_health = get_health(created_health.id, database)
#     assert retrieved_health is None
