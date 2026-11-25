from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AgriBid WorkSphere API",
    description="Project Management and Team Collaboration Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AgriBid WorkSphere API",
        "status": "running"
    }


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "worksphere-backend"
    }