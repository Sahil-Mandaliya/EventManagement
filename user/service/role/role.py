from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from main_app.database import get_db

from main_app.utils.utils import hash_password
from user.dto.request import AssignRoleRequestDto, RegisterUserRequestDto
from user.dto.response import AssignRoleResponseDto
from user.dto.user import UserDto
from user.repository.user.user import assign_roles, create_user


def assign_roles_to_user(assign_roles_request_dto:AssignRoleRequestDto, db: Session):
    updated_user = assign_roles(assign_roles_dto=assign_roles_request_dto, db=db)
    roles = updated_user.roles
    roles_str = []
    for role in roles:
        roles_str.append(role.name)

    response  = AssignRoleResponseDto(
        username=updated_user.username,
        roles=roles_str
    )
    return response