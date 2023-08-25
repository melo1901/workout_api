from sqlalchemy import ForeignKey, Column, String, Date, Integer
from models.base import Base

class Activity(Base):
    __tablename__ = "activity"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), ForeignKey("user.nickname"))
    activity = Column(String(50))
    duration = Column(String(50))
    kcal_burnt = Column(Integer)
    date = Column(Date)
    
    def __init__(self, nickname, activity, duration, kcal_burnt, date):
        self.nickname = nickname
        self.activity = activity
        self.duration = duration
        self.kcal_burnt = kcal_burnt
        self.date = date
        
    def __repr__(self):
        return "<Activity(nickname='%s', activity='%s', duration='%s', kcal_burnt='%s', date='%s')>" % (
            self.nickname, self.activity, self.duration, self.kcal_burnt, self.date)