from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cover_letter import CoverLetter
from app.models.user import User
from app.schemas.cover_letter import (
    CoverLetterCreate,
    CoverLetterUpdate,
    CoverLetterResponse
)
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/cover-letters",
    tags=["Cover Letters"]
)


@router.get("/test")
def test_cover_letter():
    return {
        "message": "Cover Letter Router Working"
    }
    
@router.post("/", response_model=CoverLetterResponse)
def create_cover_letter(
    cover_letter: CoverLetterCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_cover_letter = CoverLetter(
        title=cover_letter.title,
        content=cover_letter.content,
        company=cover_letter.company,
        owner_id=current_user.id
    )

    db.add(new_cover_letter)
    db.commit()
    db.refresh(new_cover_letter)

    return new_cover_letter

@router.get("/", response_model=list[CoverLetterResponse])
def get_cover_letters(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cover_letters = db.query(CoverLetter).filter(
        CoverLetter.owner_id == current_user.id
    ).all()

    return cover_letters

@router.get("/{cover_letter_id}", response_model=CoverLetterResponse)
def get_cover_letter(
    cover_letter_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cover_letter = db.query(CoverLetter).filter(
        CoverLetter.id == cover_letter_id,
        CoverLetter.owner_id == current_user.id
    ).first()

    if cover_letter is None:
        raise HTTPException(
            status_code=404,
            detail="Cover Letter not found"
        )

    return cover_letter

@router.put("/{cover_letter_id}", response_model=CoverLetterResponse)
def update_cover_letter(
    cover_letter_id: int,
    cover_letter: CoverLetterUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_cover_letter = db.query(CoverLetter).filter(
        CoverLetter.id == cover_letter_id,
        CoverLetter.owner_id == current_user.id
    ).first()

    if existing_cover_letter is None:
        raise HTTPException(
            status_code=404,
            detail="Cover Letter not found"
        )

    existing_cover_letter.title = cover_letter.title
    existing_cover_letter.content = cover_letter.content
    existing_cover_letter.company = cover_letter.company

    db.commit()
    db.refresh(existing_cover_letter)

    return existing_cover_letter

@router.delete("/{cover_letter_id}")
def delete_cover_letter(
    cover_letter_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cover_letter = db.query(CoverLetter).filter(
        CoverLetter.id == cover_letter_id,
        CoverLetter.owner_id == current_user.id
    ).first()

    if cover_letter is None:
        raise HTTPException(
            status_code=404,
            detail="Cover Letter not found"
        )

    db.delete(cover_letter)
    db.commit()

    return {
        "message": "Cover Letter deleted successfully"
    }