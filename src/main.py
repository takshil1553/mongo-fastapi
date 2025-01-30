from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.urls import router as router

app = FastAPI(title="FastAPI + MongoDB", version="1.0")

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(router)

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB"}

# Run with: `uvicorn main:app
