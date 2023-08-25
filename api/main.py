from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models.activity import Activity
from models.user import User
from models.base import Base

db_url = "mysql+mysqlconnector://root:password@localhost:3306/api"

try:
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    user = User(nickname="test", name="Test", surname="Test", email="test", join_date="2018-01-01")
    activity = Activity(nickname="test", activity="test2", duration="test2", kcal_burnt=2, date="2018-01-02")
    session.add(activity)
    session.commit()
    
except SQLAlchemyError as e:
    print("Connection failed: ", e)