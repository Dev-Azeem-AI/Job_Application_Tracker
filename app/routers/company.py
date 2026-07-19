from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.company import Company
from app.models.user import User
from app.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
    CompanyResponse
)
from app.auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.post("/", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_company = Company(
        name=company.name,
        location=company.location,
        website=company.website,
        hr_name=company.hr_name,
        hr_email=company.hr_email,
        phone=company.phone,
        priority=company.priority,
        notes=company.notes,
        owner_id=current_user.id
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company

@router.get("/", response_model=list[CompanyResponse])
def get_companies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    companies = db.query(Company).filter(
        Company.owner_id == current_user.id
    ).all()

    return companies

@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    company = db.query(Company).filter(
        Company.id == company_id,
        Company.owner_id == current_user.id
    ).first()

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company

@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_company = db.query(Company).filter(
        Company.id == company_id,
        Company.owner_id == current_user.id
    ).first()

    if existing_company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    existing_company.name = company.name
    existing_company.location = company.location
    existing_company.website = company.website
    existing_company.hr_name = company.hr_name
    existing_company.hr_email = company.hr_email
    existing_company.phone = company.phone
    existing_company.priority = company.priority
    existing_company.notes = company.notes

    db.commit()
    db.refresh(existing_company)

    return existing_company

@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    company = db.query(Company).filter(
        Company.id == company_id,
        Company.owner_id == current_user.id
    ).first()

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    db.delete(company)
    db.commit()

    return {
        "message": "Company deleted successfully"
    }