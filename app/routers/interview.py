from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.interview import Interview
from app.models.user import User
from app.schemas.interview import (
    InterviewCreate,
    InterviewUpdate,
    InterviewResponse
)
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)


@router.get("/test")
def test_interview():
    return {
        "message": "Interview Router Working"
    }
    
@router.post("/", response_model=InterviewResponse)
def create_interview(
    interview: InterviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_interview = Interview(
        company=interview.company,
        position=interview.position,
        interview_date=interview.interview_date,
        interview_time=interview.interview_time,
        round=interview.round,
        status=interview.status,
        notes=interview.notes,
        owner_id=current_user.id
    )

    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)

    return new_interview

@router.get("/", response_model=list[InterviewResponse])
def get_interviews(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    interviews = db.query(Interview).filter(
        Interview.owner_id == current_user.id
    ).all()

    return interviews

@router.get("/{interview_id}", response_model=InterviewResponse)
def get_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id,
        Interview.owner_id == current_user.id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    return interview

@router.put("/{interview_id}", response_model=InterviewResponse)
def update_interview(
    interview_id: int,
    interview: InterviewUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_interview = db.query(Interview).filter(
        Interview.id == interview_id,
        Interview.owner_id == current_user.id
    ).first()

    if existing_interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    existing_interview.company = interview.company
    existing_interview.position = interview.position
    existing_interview.interview_date = interview.interview_date
    existing_interview.interview_time = interview.interview_time
    existing_interview.round = interview.round
    existing_interview.status = interview.status
    existing_interview.notes = interview.notes

    db.commit()
    db.refresh(existing_interview)

    return existing_interview

@router.delete("/{interview_id}")
def delete_interview(
    interview_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    interview = db.query(Interview).filter(
        Interview.id == interview_id,
        Interview.owner_id == current_user.id
    ).first()

    if interview is None:
        raise HTTPException(
            status_code=404,
            detail="Interview not found"
        )

    db.delete(interview)
    db.commit()

    return {
        "message": "Interview deleted successfully"
    }