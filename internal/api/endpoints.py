from fastapi import APIRouter, Depends, Request
from auth.decorator import has_roles
from main_app.database import get_db
from sqlalchemy.orm import Session

from user.dto.request import AssignRoleRequestDto, RegisterUserRequestDto
from user.dto.response import AssignRoleResponseDto
from user.dto.user import UserDto
from user.service.role.role import assign_roles_to_user
from user.service.user.register import register_user

api_router = APIRouter()

@api_router.post("/user/register", response_model=UserDto)
@has_roles(["admin"])
def register_internal_user_api(
        request: Request,
        payload: RegisterUserRequestDto, 
        db: Session = Depends(get_db)
    ):
    # Add validations
    return register_user(payload, db, True)


@api_router.post("/role/assign", response_model=AssignRoleResponseDto)
@has_roles(["admin"])
def assign_role_api(request: Request, payload: AssignRoleRequestDto, db: Session = Depends(get_db)):
    # Add validations
    return assign_roles_to_user(payload, db)
