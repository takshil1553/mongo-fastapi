from motor.motor_asyncio import AsyncIOMotorClient
from src.db.config import MONGO_URI, DATABASE_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

async def get_db():
    return db
