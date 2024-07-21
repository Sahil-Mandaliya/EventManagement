from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from main_app.database import Base
from main_app.models import TimeStampModel

user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

class User(TimeStampModel):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100), index=True, nullable=False)    
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(15), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200))
    
    roles = relationship("Role", secondary=user_roles, back_populates="users")


class Role(TimeStampModel):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    
    users = relationship("User", secondary=user_roles, back_populates="roles")
