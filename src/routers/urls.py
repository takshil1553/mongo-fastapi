from fastapi import APIRouter, Query
from src.services.user.controller import (
    handle_create_user,
    handle_get_users,
    handle_get_user_by_id,
    handle_update_user
)
from src.services.user.schema import UserCreate, UserQuery, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=dict)
async def create_user(user: UserCreate):
    return await handle_create_user(user)

@router.get("/", response_model=list)
async def get_users(
    name: str = Query(None, description="Filter by name"),
    email: str = Query(None, description="Filter by email"),
    min_age: int = Query(None, description="Filter by minimum age"),
    max_age: int = Query(None, description="Filter by maximum age")
):
    query = UserQuery(name=name, email=email, min_age=min_age, max_age=max_age)
    return await handle_get_users(query)

@router.get("/{user_id}", response_model=dict)
async def get_user_by_id(user_id: str):
    return await handle_get_user_by_id(user_id)

@router.put("/{user_id}", response_model=dict)
async def update_user(user_id: str, user_update: UserUpdate):
    return await handle_update_user(user_id, user_update)
