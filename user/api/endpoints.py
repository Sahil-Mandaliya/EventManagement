from fastapi import APIRouter, Depends
from main_app.database import get_db
from sqlalchemy.orm import Session

from user.dto.request import RegisterUserRequestDto
from user.dto.user import UserDto
from user.service.user.register import register_user

api_router = APIRouter()

@api_router.post("/register", response_model=UserDto)
def register_user_api(payload: RegisterUserRequestDto, db: Session = Depends(get_db)):
    # Add validations
    return register_user(payload, db)

