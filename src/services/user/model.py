from typing import Optional
from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    name: str
    email: Optional[EmailStr] 
    age: Optional[int] = None
