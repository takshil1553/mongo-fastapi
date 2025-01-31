from fastapi import APIRouter, Request
from src.services.user.controller import UserController
from src.services.user.serializer import UserRequestSerializer, UserResponseSerializer
from typing import List
from fastapi import APIRouter

router = APIRouter()
@router.post("/create_user")
async def create_user(request: Request, user_data: UserRequestSerializer):
    return await UserController.create_user(request, user_data)

@router.get("/get_user/{user_id}")
async def get_user(request: Request, user_id: str):
    return await UserController.get_user(request, user_id)

@router.put("/update_user/{user_id}")
async def update_user(request: Request, user_id: str, user_data: UserRequestSerializer):
    return await UserController.update_user(request, user_id, user_data)

@router.delete("/delete_user/{user_id}")
async def delete_user(request: Request, user_id: str):
    return await UserController.delete_user(request, user_id)

