import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import base, user, health, activity
from dotenv import load_dotenv

load_dotenv()

try:
    if os.environ["ENVIRONMENT"] == "test":
        db_url = os.environ["test_db"]
    else:
        db_url = os.environ["db"]
except KeyError as e:
    raise Exception(f"Missing required environment variable: {e}")

try:
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
except Exception as e:
    raise Exception(f"Failed to connect to database: {e}")

base.Base.metadata.create_all(engine)
