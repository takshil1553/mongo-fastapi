from fastapi import HTTPException
from typing import List
# from src.db.database import client  # Assuming client is set in app.state.db
from src.services.user.model import User
from src.services.user.serializer import UserRequestSerializer, UserResponseSerializer
from bson import ObjectId  # For handling ObjectId
from fastapi import Request

class UserService:

    @classmethod
    async def create_user(
        cls,
        request: Request, 
        user_data: UserRequestSerializer
    ) :
        db = request.app.state.db  # Access MongoDB
        users_collection = db.get_collection('users')

        user_dict = user_data.model_dump()

        result = await users_collection.insert_one(user_dict)

        if not result.inserted_id:
            raise Exception("Failed to insert user")

        return {
            "id": str(result.inserted_id),
            **user_dict
        }

    @classmethod
    async def get_user(cls, request: Request, user_id: str):
        db = request.app.state.db
        users_collection = db.get_collection('users')

        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            return None

        user["id"] = str(user["_id"])
        del user["_id"]
        return user

    @classmethod
    async def update_user(cls, request: Request, user_id: str, user_data: UserRequestSerializer):
        db = request.app.state.db
        users_collection = db.get_collection('users')

        user_dict = user_data.model_dump()
        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user_dict}
        )

        if result.modified_count == 0:
            return None

        updated_user = await users_collection.find_one({"_id": ObjectId(user_id)})
        updated_user["id"] = str(updated_user["_id"])
        del updated_user["_id"]
        return updated_user
    
    @classmethod
    async def delete_user(cls, request: Request, user_id: str):
        db = request.app.state.db
        users_collection = db.get_collection('users')

        result = await users_collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
