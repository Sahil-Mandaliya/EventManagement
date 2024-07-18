from typing import List, Optional
from pydantic import BaseModel

from user.dto.user import RoleDto

class RegisterUserRequestDto(BaseModel):
    full_name: str
    username: str
    email: Optional[str]
    phone: str
    password: str

class AssignRoleRequestDto(BaseModel):
    username: str
    roles: List[str]


