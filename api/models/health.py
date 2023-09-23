from sqlalchemy import ForeignKey, Column, String, Integer
from api.models.base import Base
from pydantic import BaseModel

class Health(Base):
    __tablename__ = "health"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), ForeignKey("user.nickname"))
    blood_pressure = Column(String(50))
    pulse = Column(Integer)
    
    def __init__(self, nickname, blood_pressure, pulse):
        self.nickname = nickname
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        
    def __repr__(self):
        return "<Health(nickname='%s', blood_pressure='%s', pulse='%s')>" % (
            self.nickname, self.blood_pressure, self.pulse)
    

class HealthBase(BaseModel):
    nickname: str
    blood_pressure: str
    pulse: int

class HealthCreate(HealthBase):
    pass

class HealthUpdate(HealthBase):
    pass

class Health(HealthBase):
    id: int

    class Config:
        from_attributes = True