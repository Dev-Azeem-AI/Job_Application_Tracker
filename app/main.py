from fastapi import FastAPI

app = FastAPI(
    title="Job Application Tracker API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Job Application Tracker API"
    }