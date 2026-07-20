from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database import get_db
from app.models.job import Job
from app.models.user import User
from app.schemas.job import JobCreate, JobUpdate, JobResponse
from app.auth.oauth2 import get_current_user
from fastapi import Query

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.post("/", response_model=JobResponse)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_job = Job(
        company=job.company,
        position=job.position,
        status=job.status,
        owner_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job

@router.get("/", response_model=list[JobResponse])
def get_jobs(
    search: str = Query(default=""),
    status: str = Query(default=""),
    sort: str = Query(default="desc"),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1),

    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Job).filter(
        Job.owner_id == current_user.id
    )

    if search:
        query = query.filter(
            Job.company.ilike(f"%{search}%")
        )

    if status:
        query = query.filter(
            Job.status == status
        )

    if sort == "asc":
        query = query.order_by(Job.applied_date.asc())
    else:
        query = query.order_by(Job.applied_date.desc())

    jobs = query.offset(skip).limit(limit).all()

    return jobs

@router.put("/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    job: JobUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_job = db.query(Job).filter(
        Job.id == job_id,
        Job.owner_id == current_user.id
    ).first()

    if existing_job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    existing_job.company = job.company
    existing_job.position = job.position
    existing_job.status = job.status

    db.commit()
    db.refresh(existing_job)

    return existing_job

@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.owner_id == current_user.id
    ).first()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    db.delete(job)
    db.commit()

    return {
        "message": "Job deleted successfully"
    }