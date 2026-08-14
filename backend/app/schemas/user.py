from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    full_name:str
    nick_name:Optional[str]=None
    email:EmailStr
    password:str=None
    
    model_config=ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    full_name:Optional[str]=None
    nick_name:Optional[str]=None
    email:Optional[EmailStr]=None
    #password:Optional[str]=None
    
class UserResponse(BaseModel):
    id:int
    full_name:str
    nick_name:str
    email:EmailStr
    #password:str
    created_at:datetime
    updated_at:datetime
    