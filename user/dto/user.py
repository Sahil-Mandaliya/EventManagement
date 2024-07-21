from typing import Optional
from pydantic import BaseModel

class UserResponse(BaseModel):
    full_name: str
    username: str
    email: str
    phone: str

class UserDto(BaseModel):
    full_name: str
    username: str
    email: str
    phone: str
    hashed_password: Optional[str]
    
    class Config:
        orm_mode = True

class RoleDto(BaseModel):
    role: str