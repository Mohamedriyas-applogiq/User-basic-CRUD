from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from configuration.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    email = Column(String(length=255), unique=True, index=True)  
    password = Column(String(length=255)) 
    is_active = Column(Boolean, default=True)

    

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    title = Column(String(length=255), index=True)  
    description = Column(String(length=500), index=True)  
    owner_id = Column(Integer, ForeignKey("users.id"))

    





















