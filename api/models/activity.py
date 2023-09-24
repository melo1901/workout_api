from sqlalchemy import ForeignKey, Column, String, Date, Integer
from api.models.base import Base
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import relationship

class Activity(Base):
    __tablename__ = "activity"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), ForeignKey("user.nickname"))
    activity = Column(String(50))
    duration = Column(String(50))
    kcal_burnt = Column(Integer)
    date = Column(Date)
    user = relationship("User", back_populates="activities")
    
    def __init__(self, nickname, activity, duration, kcal_burnt, date):
        self.nickname = nickname
        self.activity = activity
        self.duration = duration
        self.kcal_burnt = kcal_burnt
        self.date = date
        
    def __repr__(self):
        return "<Activity(nickname='%s', activity='%s', duration='%s', kcal_burnt='%s', date='%s')>" % (
            self.nickname, self.activity, self.duration, self.kcal_burnt, self.date)

class ActivityCreate(BaseModel):
    nickname: str
    activity: str
    duration: str
    kcal_burnt: int
    date: date

class ActivityUpdate(BaseModel):
    activity: str
    duration: str
    kcal_burnt: int
    date: date

class ActivityResponse(BaseModel):
    id: int
    nickname: str
    activity: str
    duration: str
    kcal_burnt: int
    date: date