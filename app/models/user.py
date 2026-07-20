from sqlalchemy import Boolean, Column, DateTime, Integer, String
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    
    jobs = relationship(
    "Job",
    back_populates="owner",
    cascade="all, delete"
)
    companies = relationship(
    "Company",
    back_populates="owner",
    cascade="all, delete"
)
    
    resumes = relationship(
    "Resume",
    back_populates="owner",
    cascade="all, delete"
)
    
    cover_letters = relationship(
    "CoverLetter",
    back_populates="owner",
    cascade="all, delete"
)
    
interviews = relationship(
    "Interview",
    back_populates="owner",
    cascade="all, delete"
)

notifications = relationship(
    "Notification",
    back_populates="owner",
    cascade="all, delete"
)