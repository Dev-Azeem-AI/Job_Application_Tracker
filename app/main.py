from fastapi import FastAPI

from app.database import engine, Base

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