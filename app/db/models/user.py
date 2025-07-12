# app/db/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)

    # ⬇️  relación inversa
    readings = relationship(
        "Reading",
        back_populates="user",
        cascade="all, delete-orphan",
    )
