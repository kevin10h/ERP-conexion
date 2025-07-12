# app/db/models/reading.py
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.base import Base
import time


class Reading(Base):
    __tablename__ = "readings"

    id          = Column(Integer, primary_key=True, index=True)
    heart_rate  = Column(Integer)
    spo2        = Column(Integer)
    respiration = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    user    = relationship("User", back_populates="readings")
    
    ts = Column(Integer, default=lambda: int(time.time()), nullable=False)
