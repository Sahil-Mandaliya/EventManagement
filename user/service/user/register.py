from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from main_app.utils.utils import hash_password
from user.dto.request import RegisterUserRequestDto
from user.dto.user import UserDto
from user.models.user import User
from user.repository.user.user import assign_roles, create_user, get_user_by_parameter, update_password

def is_existing_user(username=None, email=None, phone=None, db:Session = None):
    existing_user = None
    if username:
        existing_user = get_user_by_parameter("username",username, db)
    
    if email:
        existing_user = get_user_by_parameter("email",email, db)

    if phone:
        existing_user = get_user_by_parameter("phone",phone, db)
    
    return existing_user

def register_user(user_request_dto:RegisterUserRequestDto, db: Session, is_internal:bool=False):
    user_dto = UserDto(
        full_name=user_request_dto.full_name,
        username = user_request_dto.username,
        email = user_request_dto.email,
        phone=user_request_dto.phone,
        hashed_password = hash_password(user_request_dto.password)
    )
    
    existing_user: User = is_existing_user(user_request_dto.username,  user_request_dto.email, user_request_dto.phone, db)
    if existing_user:
        if is_internal and existing_user.hashed_password and user_dto.hashed_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Already exists")
        
        if is_internal and not user_dto.hashed_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password is required to register user")
        
        if is_internal and not existing_user.hashed_password and user_dto.hashed_password:
            existing_user = update_password(existing_user, user_dto.hashed_password, db)
            return existing_user
                    
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Already exists")

    created_user = create_user(user_dto=user_dto, db=db)
    if user_request_dto.roles:
        created_user = assign_roles(created_user.username, user_request_dto.roles)

    return created_user
