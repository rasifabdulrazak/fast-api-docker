from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,Boolean
from sqlalchemy.sql import func
from config.db import Base


class BaseModel(Base):
    __abstract__ = True
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean,default=False)