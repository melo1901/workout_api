from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from api.database import session

router = APIRouter()


@router.get("")
async def db_check():
    try:
        session.execute(text("SELECT 1"))
        return {"status": "Database connection successful"}
    except OperationalError:
        raise HTTPException(status_code=500, detail="Database connection failed")
