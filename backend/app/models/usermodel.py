from app.core.database import Base
from sqlalchemy import Column,String,Integer,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    full_name=Column(String,nullable=False)
    nick_name=Column(String,nullable=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    items=relationship("Items",back_populates="user")
    image=relationship("Image",back_populates="user")