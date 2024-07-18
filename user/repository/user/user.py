

from sqlalchemy.orm import Session

from user.dto.request import AssignRoleRequestDto
from user.models.user import Role, User
from user.dto.user import UserDto


def create_user(user_dto: UserDto, db: Session):
    user = User(
        full_name=user_dto.full_name,
        username=user_dto.username,
        email=user_dto.email,
        phone=user_dto.phone,
        hashed_password=user_dto.hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def assign_roles(assign_roles_dto:AssignRoleRequestDto, db:Session):
    roles = db.query(Role).filter(Role.name.in_(assign_roles_dto.roles)).all()
    user = db.query(User).filter(User.username == assign_roles_dto.username).first()
    if not user:
        raise ValueError("User not found")

    if not roles:
        raise ValueError("Roles not found")

    user.roles = roles
    db.commit()
    db.refresh(user)
    return user

