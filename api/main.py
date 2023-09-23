from fastapi.applications import FastAPI
from fastapi.routing import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()