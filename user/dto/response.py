
from typing import List
from pydantic import BaseModel

from main_app.api import ApiResponse
from user.dto.user import UserResponse


class RegisterUserResponse(ApiResponse):
    data: UserResponse
    pass

class AssignRoleResponseDto(BaseModel):
    username: str
    roles: List[str]


class LoginResponseDto(BaseModel):
    message: str
