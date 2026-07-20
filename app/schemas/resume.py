from pydantic import BaseModel


class ResumeCreate(BaseModel):
    title: str
    file_path: str
    description: str | None = None


class ResumeUpdate(BaseModel):
    title: str
    file_path: str
    description: str | None = None


class ResumeResponse(BaseModel):
    id: int
    title: str
    file_path: str
    description: str | None
    owner_id: int

    class Config:
        from_attributes = True