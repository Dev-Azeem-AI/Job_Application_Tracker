from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String, nullable=False)

    position = Column(String, nullable=False)

    interview_date = Column(Date, nullable=False)

    interview_time = Column(Time, nullable=False)

    round = Column(String, nullable=False)

    status = Column(String, default="Scheduled")

    notes = Column(String)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="interviews"
    )