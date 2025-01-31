import logging
from fastapi import HTTPException, status, Request
from src.services.user.schema import UserService
from src.services.user.serializer import (
    UserRequestSerializer,
    UserResponseSerializer
)
from typing import List
from src.utils.response import response_structure,SuccessResponseSerializer

class UserController:
    @classmethod
    async def create_user(
        cls,
        request: Request,  # ✅ Accept request explicitly
        user_data: UserRequestSerializer
    ):
        try:
            user = await UserService.create_user(request, user_data)
            serializer = SuccessResponseSerializer(
                status_code = status.HTTP_200_OK,
                message = "User created successfully",
                data = UserResponseSerializer.model_validate(user)
            )
            logging.info("Returning User Creation Response")
            return response_structure(
                serializer = serializer,
                status_code = status.HTTP_200_OK
            )
        except Exception as e:
            logging.error(f"Error in create_user: {e}")
            raise HTTPException(
                status_code=500, 
                detail=str(e)
            )

    @classmethod
    async def get_user(cls, request: Request, user_id: str):
        try:
            user = await UserService.get_user(request, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            
            serializer = SuccessResponseSerializer(
                status_code=status.HTTP_200_OK,
                message="User retrieved successfully",
                data=UserResponseSerializer.model_validate(user)
            )
            
            logging.info("Returning User Data")
            return response_structure(serializer=serializer, status_code=status.HTTP_200_OK)

        except Exception as e:
            logging.error(f"Error in get_user: {e}")
            raise HTTPException(status_code=500, detail=str(e))
    
    @classmethod
    async def update_user(cls, request: Request, user_id: str, user_data: UserRequestSerializer):
        try:
            updated_user = await UserService.update_user(request, user_id, user_data)
            if not updated_user:
                raise HTTPException(status_code=404, detail="User not found or update failed")

            serializer = SuccessResponseSerializer(
                status_code=status.HTTP_200_OK,
                message="User updated successfully",
                data=UserResponseSerializer.model_validate(updated_user)
            )

            logging.info("Returning Updated User Data")
            return response_structure(serializer=serializer, status_code=status.HTTP_200_OK)

        except Exception as e:
            logging.error(f"Error in update_user: {e}")
            raise HTTPException(status_code=500, detail=str(e))


    @classmethod
    async def delete_user(cls, request: Request, user_id: str):
        try:
            deleted = await UserService.delete_user(request, user_id)
            if not deleted:
                raise HTTPException(status_code=404, detail="User not found or already deleted")

            serializer = SuccessResponseSerializer(
                status_code=status.HTTP_200_OK,
                message="User deleted successfully",
                data={}
            )

            logging.info("User deleted successfully")
            return response_structure(serializer=serializer, status_code=status.HTTP_200_OK)

        except Exception as e:
            logging.error(f"Error in delete_user: {e}")
            raise HTTPException(status_code=500, detail=str(e))