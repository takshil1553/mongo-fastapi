from pydantic import BaseModel, EmailStr, conint
from uuid import UUID
from typing import List
from typing import Optional
class UserRequestSerializer(BaseModel):
    name: str
    email: EmailStr
    age: Optional[conint(ge=0)] = None  # Ensure age is non-negative (if provided)

    class Config:
        # ORM Mode will allow us to serialize and deserialize with ORM models
        from_attributes = True

class UserResponseSerializer(UserRequestSerializer):
    id: str