from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_jobs: int
    total_companies: int
    applied: int
    interview: int
    offer: int
    rejected: int
    wishlist: int