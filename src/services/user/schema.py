from pydantic import BaseModel, EmailStr
from typing import Optional, List
from bson import ObjectId

# 🟢 Serializer: Converts MongoDB Object to JSON Response
class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr 
    age: Optional[int]

    @classmethod
    def serialize(cls,user) -> dict:
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "age": user.get("age"),
        }

    @classmethod
    def serialize_list(cls,users) -> List[dict]:
        return [UserResponse.serialize(user) for user in users]

# 🟢 Request Schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

# 🟢 Query Schema (Filtering Users)
class UserQuery(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    min_age: Optional[int] = None
    max_age: Optional[int] = None

    def build_query(self) -> dict:
        query = {}

        if self.name:
            query["name"] = {"$regex": self.name, "$options": "i"}  # Case-insensitive
        if self.email:
            query["email"] = self.email
        if self.min_age is not None:
            query["age"] = {"$gte": self.min_age}
        if self.max_age is not None:
            query.setdefault("age", {})["$lte"] = self.max_age

        return query
