from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.urls import router as router
from motor.motor_asyncio import AsyncIOMotorClient
from src.db.database import startup_db, shutdown_db  # Include DB setup methods

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
@app.on_event("startup")
async def startup_db_client():
    app.state.db = AsyncIOMotorClient("mongodb://localhost:27017")["test2"]

@app.on_event("shutdown")
async def on_shutdown():
    await shutdown_db(app)

app.include_router(router)  

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB"}
