from pydantic import BaseModel


class CoverLetterCreate(BaseModel):
    title: str
    content: str
    company: str


class CoverLetterUpdate(BaseModel):
    title: str
    content: str
    company: str


class CoverLetterResponse(BaseModel):
    id: int
    title: str
    content: str
    company: str
    owner_id: int

    class Config:
        from_attributes = True