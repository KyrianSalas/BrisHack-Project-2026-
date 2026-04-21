import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.satellites import router as satellites_router
from core.config import settings

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Satellite Tracking API", version="1.0")

default_origins = [
    "https://www.navsat.co.uk",
    "https://navsat.co.uk",
    "http://localhost:5173",
]

allowed_origins = default_origins
if settings.cors_allowed_origins:
    allowed_origins = [
        origin.strip()
        for origin in settings.cors_allowed_origins.split(",")
        if origin.strip()
    ]

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(satellites_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Satellite Tracking API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)