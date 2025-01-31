from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# MongoDB URI and Database name from environment variables or fallback to default
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Use environment variable if available
DATABASE_NAME = os.getenv("DATABASE_NAME", "test2")  # Database name

# Global variable to store the database client
client: AsyncIOMotorClient = None

# Initialize the MongoDB client and database on FastAPI startup
async def startup_db(app: FastAPI):
    """Initialize the MongoDB connection on startup"""
    global client
    client = AsyncIOMotorClient(MONGO_URI)  # Use the async MongoDB client
    db = client[DATABASE_NAME]  # Use 'test2' database directly
    app.state.db = db  # Attach the db to FastAPI's app state

async def shutdown_db(app: FastAPI):
    """Clean up MongoDB connection on shutdown"""
    if client:
        client.close()  # Close the MongoDB client connection

# FastAPI app initialization
app = FastAPI()

# FastAPI event handlers for startup and shutdown
@app.on_event("startup")
async def on_startup():
    await startup_db(app)

@app.on_event("shutdown")
async def on_shutdown():
    await shutdown_db(app)
