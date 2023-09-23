from sqlalchemy import Column, String, Date
from api.models.base import Base

class User(Base):
    __tablename__ = "user"
    
    nickname = Column(String(50), unique=True, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50), unique=True)
    join_date = Column(Date)
    
    def __init__(self, nickname, name, surname, email, join_date):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.email = email
        self.join_date = join_date
        
    def __repr__(self):
        return "<User(nickname='%s', name='%s', surname='%s', email='%s', join_date='%s')>" % (
            self.nickname, self.name, self.surname, self.email, self.join_date)

