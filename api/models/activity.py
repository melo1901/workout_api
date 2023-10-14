from typing import Optional
from sqlalchemy import ForeignKey, Column, String, Integer
from api.models.base import Base
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), ForeignKey("users.nickname"))
    activity = Column(String(50))
    duration = Column(String(50))
    kcal_burned = Column(Integer)
    date = Column(String(50))
    users = relationship("Users", back_populates="activities")

    def __init__(self, nickname, activity, duration, kcal_burned, date):
        self.nickname = nickname
        self.activity = activity
        self.duration = duration
        self.kcal_burned = kcal_burned
        self.date = date

    def __repr__(self):
        return (
            "<Activity(nickname='%s', activity='%s', duration='%s', kcal_burned='%s', date='%s')>"
            % (self.nickname, self.activity, self.duration, self.kcal_burned, self.date)
        )


class ActivityBase(BaseModel):
    nickname: str
    activity: str
    duration: str
    kcal_burned: int
    date: str


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdateSchema(BaseModel):
    activity: Optional[str] = Field(default=None)
    duration: Optional[str] = Field(default=None)
    kcal_burned: Optional[int] = Field(default=None)
    date: Optional[str] = Field(default=None)


class ActivityUpdate(ActivityUpdateSchema):
    pass


class ActivityResponse(BaseModel):
    id: int
    nickname: str
    activity: str
    duration: str
    kcal_burned: int
    date: str
