import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import base, user, health, activity
from dotenv import load_dotenv

load_dotenv()


if os.getenv("ENVIRONMENT") == "test":
    db_url = os.getenv("test_db")
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()
else:
    db_url = os.getenv("db")
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

base.Base.metadata.create_all(engine)
