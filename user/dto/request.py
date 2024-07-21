from typing import List, Optional
from pydantic import BaseModel

class RegisterUserRequestDto(BaseModel):
    full_name: str
    username: Optional[str]
    email: str
    phone: Optional[str]
    password: str
    roles: Optional[List[str]]

class AssignRoleRequestDto(BaseModel):
    username: str
    roles: List[str]


class LoginRequestDto(BaseModel):
    username: str
    password: str

