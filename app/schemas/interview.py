from pydantic import BaseModel
from datetime import date, time


class InterviewCreate(BaseModel):
    company: str
    position: str
    interview_date: date
    interview_time: time
    round: str
    status: str
    notes: str | None = None


class InterviewUpdate(BaseModel):
    company: str
    position: str
    interview_date: date
    interview_time: time
    round: str
    status: str
    notes: str | None = None


class InterviewResponse(BaseModel):
    id: int
    company: str
    position: str
    interview_date: date
    interview_time: time
    round: str
    status: str
    notes: str | None
    owner_id: int

    class Config:
        from_attributes = True