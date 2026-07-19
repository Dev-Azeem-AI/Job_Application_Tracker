from pydantic import BaseModel
from datetime import datetime


class JobCreate(BaseModel):
    company: str
    position: str
    status: str = "Applied"


class JobUpdate(BaseModel):
    company: str
    position: str
    status: str


class JobResponse(BaseModel):
    id: int
    company: str
    position: str
    status: str
    applied_date: datetime
    owner_id: int

    class Config:
        from_attributes = True