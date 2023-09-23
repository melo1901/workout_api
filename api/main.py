from fastapi.applications import FastAPI
from fastapi.routing import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:postgres@localhost:5432/test"
engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
activity = {
    "nickname": "test",
    "activity": "test3",
    "duration": "test2",
    "kcal_burnt": 5,
    "date": "2018-01-02",
}
session = Session()

app = FastAPI()