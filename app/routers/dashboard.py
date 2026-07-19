from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.job import Job
from app.models.company import Company
from app.models.user import User
from app.schemas.dashboard import DashboardResponse
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/", response_model=DashboardResponse)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total_jobs = db.query(Job).filter(
        Job.owner_id == current_user.id
    ).count()

    total_companies = db.query(Company).filter(
        Company.owner_id == current_user.id
    ).count()

    applied = db.query(Job).filter(
        Job.owner_id == current_user.id,
        Job.status == "Applied"
    ).count()

    interview = db.query(Job).filter(
        Job.owner_id == current_user.id,
        Job.status == "Interview"
    ).count()

    offer = db.query(Job).filter(
        Job.owner_id == current_user.id,
        Job.status == "Offer"
    ).count()

    rejected = db.query(Job).filter(
        Job.owner_id == current_user.id,
        Job.status == "Rejected"
    ).count()

    wishlist = db.query(Job).filter(
        Job.owner_id == current_user.id,
        Job.status == "Wishlist"
    ).count()

    return DashboardResponse(
        total_jobs=total_jobs,
        total_companies=total_companies,
        applied=applied,
        interview=interview,
        offer=offer,
        rejected=rejected,
        wishlist=wishlist
    )