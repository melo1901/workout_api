from typing import Optional
from sqlalchemy import Column, String, Date, DOUBLE_PRECISION
from sqlalchemy.orm import relationship
from api.models.base import Base
from pydantic import BaseModel, Field
from datetime import date


class Users(Base):
    __tablename__ = "users"

    nickname = Column(String(50), unique=True, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    height = Column(DOUBLE_PRECISION)
    email = Column(String(50), unique=True)
    join_date = Column(Date)
    activities = relationship("Activity", back_populates="users")
    health_history = relationship("Health", back_populates="users")

    def __init__(self, nickname, name, surname, height, email, join_date):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.height = height
        self.email = email
        self.join_date = join_date

    def __repr__(self):
        return (
            "<Users(nickname='%s', name='%s', surname='%s', height='%s' email='%s', join_date='%s')>"
            % (
                self.nickname,
                self.name,
                self.surname,
                self.height,
                self.email,
                self.join_date,
            )
        )


class UserCreate(BaseModel):
    nickname: str
    name: str
    surname: str
    height: float
    email: str
    join_date: date


class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    surname: Optional[str] = Field(default=None)
    height: Optional[float] = Field(default=None)
    email: Optional[str] = Field(default=None)


class UserResponse(BaseModel):
    nickname: str
    name: str
    surname: str
    height: float
    email: str
    join_date: date
