
from typing import List
from pydantic import BaseModel


class AssignRoleResponseDto(BaseModel):
    username: str
    roles: List[str]

