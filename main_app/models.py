from main_app.database import Base
from sqlalchemy import Column, Integer, DateTime, func, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.ext.declarative import declared_attr


class BaseModel(Base):
    __abstract__ = True  # Ensure this class is not mapped to any table

    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class TimeStampModel(BaseModel):
    __abstract__ = True  # Ensure this class is not mapped to any table

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
class SoftDeleteModel(BaseModel):
    __abstract__ = True  # Ensure this class is not mapped to any table

    is_deleted = Column(Boolean, default=False, nullable=True)
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()