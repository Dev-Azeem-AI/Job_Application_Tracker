from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    location = Column(String)

    website = Column(String)

    hr_name = Column(String)

    hr_email = Column(String)

    phone = Column(String)

    priority = Column(String, default="Medium")

    notes = Column(Text)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="companies"
    )