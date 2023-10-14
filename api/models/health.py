from typing import Optional
from sqlalchemy import ForeignKey, Column, String, Integer, DOUBLE_PRECISION
from api.models.base import Base
from pydantic import BaseModel, Field
from sqlalchemy.orm import relationship


class Health(Base):
    __tablename__ = "health"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), ForeignKey("users.nickname"))
    blood_pressure = Column(String(50))
    weight = Column(DOUBLE_PRECISION)
    pulse = Column(Integer)
    users = relationship("Users", back_populates="health_history")

    def __init__(self, nickname, blood_pressure, pulse, weight):
        self.nickname = nickname
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.weight = weight

    def __repr__(self):
        return (
            "<Health(nickname='%s', blood_pressure='%s', pulse='%s', weight='%s')>"
            % (
                self.nickname,
                self.blood_pressure,
                self.pulse,
                self.weight,
            )
        )


class HealthBase(BaseModel):
    nickname: str
    blood_pressure: str
    pulse: int
    weight: float


class HealthCreate(HealthBase):
    pass


class HealthUpdate(BaseModel):
    nickname: Optional[str] = Field(default=None)
    blood_pressure: Optional[str] = Field(default=None)
    pulse: Optional[int] = Field(default=None)
    weight: Optional[float] = Field(default=None)


class HealthResponse(BaseModel):
    id: int
    nickname: str
    blood_pressure: str
    pulse: int
    weight: float
