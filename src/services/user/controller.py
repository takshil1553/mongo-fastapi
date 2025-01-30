from fastapi import HTTPException
from src.services.user.serializer import create_user, get_users, get_user_by_id, update_user
from src.services.user.schema import UserCreate, UserQuery, UserUpdate

async def handle_create_user(user: UserCreate):
    return await create_user(user)

async def handle_get_users(query: UserQuery):
    return await get_users(query)

async def handle_get_user_by_id(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def handle_update_user(user_id: str, user_update: UserUpdate):
    updated_user = await update_user(user_id, user_update.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or no changes applied")
    return updated_user
