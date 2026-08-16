from app.core.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Image(Base):
    __tablename__="images"
    
    id=Column(Integer,primary_key=True)
    uploaded_by=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    file_path=Column(String,nullable=True)
    original_filename=Column(String)
    new_filename=Column(String)
    mime_type=Column(String)
    uploaded_at=Column(DateTime,default=datetime.now)
    updatede_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    item=relationship("Items",back_populates="image")
    user=relationship("User",back_populates="image")