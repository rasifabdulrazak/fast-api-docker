from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base
import hashlib

class BaseModel(Base):
    __abstract__ = True
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean,default=False)

class User(BaseModel):
    __tablename__ = 'user'
    id  = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    phone_number = Column(String)
    email = Column(String,unique=True, index=True)
    _password = Column('password',String)
    is_superuser = Column(Boolean,default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        """Hash the password before storing."""
        self._password = hashlib.sha256(value.encode()).hexdigest()

