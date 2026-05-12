from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import detect

app = FastAPI(title="CV Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(detect.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "CV Detection API is running"}