from fastapi import APIRouter, Depends
from main_app.database import get_db
from sqlalchemy.orm import Session

from user.dto.request import  LoginRequestDto
from user.service.user.login import login_user

api_router = APIRouter()


@api_router.post("/login")
def login_user_api(request_dto: LoginRequestDto, db: Session = Depends(get_db)):
    access_token = login_user(request_dto.username, request_dto.password, db)
    return {"access_token": access_token, "token_type": "bearer"}