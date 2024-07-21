from fastapi import APIRouter, Depends, HTTPException, Request, status
from auth.decorator import has_roles
from main_app.database import get_db
from sqlalchemy.orm import Session

from user.dto.request import AssignRoleRequestDto, RegisterUserRequestDto
from user.dto.response import AssignRoleResponseDto, RegisterUserResponse
from user.dto.user import UserResponse, UserDto
from user.service.role.role import assign_roles_to_user
from user.service.user.register import register_user

api_router = APIRouter()

@api_router.post("/user/register", response_model=RegisterUserResponse)
@has_roles(["admin"])
def register_internal_user_api(
        request: Request,
        payload: RegisterUserRequestDto, 
        db: Session = Depends(get_db)
    ):
    try:
        user:UserDto = register_user(payload, db, True)
        return RegisterUserResponse(
            status="success",
            message="User Added Succesfully",
            data=UserResponse(
                full_name=user.full_name,
                username=user.username,
                email=user.email,
                phone=user.phone
            )
        )
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")



@api_router.post("/role/assign", response_model=AssignRoleResponseDto)
@has_roles(["admin"])
def assign_role_api(request: Request, payload: AssignRoleRequestDto, db: Session = Depends(get_db)):
    # Add validations
    try:
        return assign_roles_to_user(payload, db)
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
