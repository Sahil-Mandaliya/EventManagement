from pydantic import BaseModel

class UserDto(BaseModel):
    full_name: str
    username: str
    email: str
    phone: str
    hashed_password: str
    
    class Config:
        orm_mode = True

class RoleDto(BaseModel):
    role: str