from fastapi import FastAPI
from app.models.user import User
from app.database import engine, Base
from app.auth.hashing import hash_password
from app.auth.jwt_handler import create_access_token

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Application Tracker API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Job Application Tracker API"
    }
Base.metadata.create_all(bind=engine)
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