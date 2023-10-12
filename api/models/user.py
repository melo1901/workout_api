from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship
from api.models.base import Base
from pydantic import BaseModel
from datetime import date

class Users(Base):
    __tablename__ = "users"
    
    nickname = Column(String(50), unique=True, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50), unique=True)
    join_date = Column(Date)
    activities = relationship("Activity", back_populates="users")
    
    def __init__(self, nickname, name, surname, email, join_date):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.email = email
        self.join_date = join_date
        
    def __repr__(self):
        return "<Users(nickname='%s', name='%s', surname='%s', email='%s', join_date='%s')>" % (
            self.nickname, self.name, self.surname, self.email, self.join_date)
    
class UserCreate(BaseModel):
    nickname: str
    name: str
    surname: str
    email: str
    join_date: date

class UserUpdate(BaseModel):
    name: str
    surname: str
    email: str

class UserResponse(BaseModel):
    nickname: str
    name: str
    surname: str
    email: str
    join_date: date
