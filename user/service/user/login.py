from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth.auth import create_access_token, verify_password
from main_app.database import get_db

from main_app.utils.utils import hash_password
from user.dto.request import RegisterUserRequestDto
from user.dto.user import UserDto
from user.models.user import User
from user.repository.user.user import assign_roles, create_user, get_user_by_parameter


def login_user(username:str, password:str, db: Session):
    db_user:User = get_user_by_parameter("username", username, db)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password")
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": db_user.username})
    return access_token