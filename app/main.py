from fastapi import FastAPI
from app.models.user import User
from app.models.job import Job
from app.database import engine, Base
from app.auth.hashing import hash_password
from app.auth.jwt_handler import create_access_token
from app.routers import auth
from app.auth.jwt_handler import verify_access_token
from app.routers import jobs
from app.models.company import Company
from app.routers import company
from app.routers import dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Application Tracker API",
    version="1.0.0"
)
app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(company.router)
app.include_router(dashboard.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Job Application Tracker API"
    }

@app.get("/health")
def health():
    return {
        "status": "Database Connected",
        "table": "users"
    }
    



@app.get("/test-hash")
def test_hash():
    password = "123456"

    hashed = hash_password(password)

    return {
        "original": password,
        "hashed": hashed
    }
    
@app.get("/test-token")
def test_token():
    token = create_access_token(
        {"sub": "azeem@gmail.com"}
    )

    return {
        "access_token": token
    }
    
@app.get("/verify-token")
def verify_token():
    token = create_access_token(
        {"sub": "azeem@gmail.com"}
    )

    email = verify_access_token(token)

    return {
        "token": token,
        "email": email
    }