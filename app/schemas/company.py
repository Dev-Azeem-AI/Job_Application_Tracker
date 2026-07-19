from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    location: str | None = None
    website: str | None = None
    hr_name: str | None = None
    hr_email: str | None = None
    phone: str | None = None
    priority: str = "Medium"
    notes: str | None = None


class CompanyUpdate(BaseModel):
    name: str
    location: str | None = None
    website: str | None = None
    hr_name: str | None = None
    hr_email: str | None = None
    phone: str | None = None
    priority: str
    notes: str | None = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    location: str | None
    website: str | None
    hr_name: str | None
    hr_email: str | None
    phone: str | None
    priority: str
    notes: str | None
    owner_id: int

    class Config:
        from_attributes = True