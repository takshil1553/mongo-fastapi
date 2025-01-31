from mongoengine import Document, StringField, IntField
from pydantic import BaseModel
from uuid import uuid4
from src.services.user.serializer import UserResponseSerializer, UserRequestSerializer

class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    age = IntField(min_value=0, required=False)

    def to_pydantic(self):
        return UserResponseSerializer(
            id=str(self.id),  # Convert ObjectId to string
            name=self.name,
            email=self.email,
            age=self.age
        )

    @classmethod
    def from_pydantic(cls, pydantic_obj: UserRequestSerializer):
        return cls(
            name=pydantic_obj.name,
            email=pydantic_obj.email,
            age=pydantic_obj.age
        )
