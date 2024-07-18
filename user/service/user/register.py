from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from main_app.database import get_db

from main_app.utils.utils import hash_password
from user.dto.request import RegisterUserRequestDto
from user.dto.user import UserDto
from user.repository.user.user import create_user


def register_user(user_request_dto:RegisterUserRequestDto, db: Session):
    user_dto = UserDto(
        full_name=user_request_dto.full_name,
        username = user_request_dto.username,
        email = user_request_dto.email,
        phone=user_request_dto.phone,
        hashed_password = hash_password(user_request_dto.password)
    )
    
    created_user = create_user(user_dto=user_dto, db=db)
    return created_user