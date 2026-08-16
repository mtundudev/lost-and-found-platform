from app.core.database import  Base
from sqlalchemy import Column,Integer,String,DateTime,DATE,ForeignKey,Enum
import enum
from sqlalchemy.orm import relationship
from datetime import datetime

class Item_type(str,enum.Enum):
    lost="lost"
    found="found"


class StatusCheck(str,enum.Enum):
    active="ACTIVE"
    recovered="RECOVERED"
    returned="RETURNED"
  
    

class Items(Base):
    __tablename__="items"
    
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=True)
    category=Column(String)
    item_type=Column(Enum(Item_type),default=Item_type.lost)
    location=Column(String)
    date_occurred=Column(DATE)
    status=Column(Enum(StatusCheck),default=StatusCheck.active)
    image_id=Column(Integer,ForeignKey("images.id",ondelete="CASCADE"),nullable=True)
    created_by=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"))
    created_at=Column(DateTime,default=datetime.now())
    updated_at=Column(DateTime,default=datetime.now(),onupdate=datetime.now())
    
    image=relationship("Image",back_populates="item")
    user=relationship("User",back_populates="items")