from bson import ObjectId
from src.db.database import db
from src.services.user.model import UserModel
from src.services.user.schema import UserQuery, UserResponse

users_collection = db["users"]

# Create a User
async def create_user(user: UserModel):
    user_dict = user.dict()
    result = await users_collection.insert_one(user_dict)
    user_dict["_id"] = result.inserted_id
    return UserResponse.serialize(user_dict)

# Get Users with Query Filters
async def get_users(query: UserQuery):
    filters = query.build_query()
    users = await users_collection.find(filters).to_list(100)
    return UserResponse.serialize_list(users)

# Get User by ID
async def get_user_by_id(user_id: str):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    return UserResponse.serialize(user) if user else None

# Update User
async def update_user(user_id: str, user_update: dict):
    result = await users_collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": user_update}
    )
    if result.modified_count == 0:
        return None
    return await get_user_by_id(user_id)
