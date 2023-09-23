from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import base, user, health, activity

db_url = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()
base.Base.metadata.create_all(engine)