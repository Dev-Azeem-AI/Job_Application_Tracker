from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.resume import Resume
from app.models.user import User
from app.schemas.resume import (
    ResumeCreate,
    ResumeUpdate,
    ResumeResponse
)
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/resumes",
    tags=["Resume"]
)

@router.get("/test")
def test_resume():
    return {
        "message": "Resume Router Working"
    }

@router.post("/", response_model=ResumeResponse)
def create_resume(
    resume: ResumeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_resume = Resume(
        title=resume.title,
        file_path=resume.file_path,
        description=resume.description,
        owner_id=current_user.id
    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    return new_resume

@router.get("/", response_model=list[ResumeResponse])
def get_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resumes = db.query(Resume).filter(
        Resume.owner_id == current_user.id
    ).all()

    return resumes

@router.get("/{resume_id}", response_model=ResumeResponse)
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.owner_id == current_user.id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume

@router.put("/{resume_id}", response_model=ResumeResponse)
def update_resume(
    resume_id: int,
    resume: ResumeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.owner_id == current_user.id
    ).first()

    if existing_resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    existing_resume.title = resume.title
    existing_resume.file_path = resume.file_path
    existing_resume.description = resume.description

    db.commit()
    db.refresh(existing_resume)

    return existing_resume

@router.delete("/{resume_id}")
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.owner_id == current_user.id
    ).first()

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    db.delete(resume)
    db.commit()

    return {
        "message": "Resume deleted successfully"
    }