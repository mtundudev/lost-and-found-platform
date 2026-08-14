from app.core.database import Base
from sqlalchemy import Column,String,Integer,DateTime
from datetime import datetime

class RevokedToken(Base):
    __tablename__="revokedtokens"
    id=Column(Integer,primary_key=True)
    token=Column(String,nullable=False,unique=True)
    expire_at=Column(DateTime,nullable=False)
    Revoked_at=Column(DateTime,default=datetime.now)