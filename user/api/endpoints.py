from fastapi import APIRouter, Depends
from main_app.database import get_db
from sqlalchemy.orm import Session

from user.dto.request import AssignRoleRequestDto, RegisterUserRequestDto
from user.dto.response import AssignRoleResponseDto
from user.dto.user import UserDto
from user.service.role.role import assign_roles_to_user
from user.service.user.register import register_user

api_router = APIRouter()

@api_router.post("/register", response_model=UserDto)
def register_user_api(payload: RegisterUserRequestDto, db: Session = Depends(get_db)):
    return register_user(payload, db)


@api_router.post("/assign", response_model=AssignRoleResponseDto)
def assign_role_api(payload: AssignRoleRequestDto, db: Session = Depends(get_db)):
    return assign_roles_to_user(payload, db)
