from pydantic import BaseModel,Field,ConfigDict
from datetime import date,datetime
from typing import Optional,List
from app.models.item import Item_type

class ItemCreate(BaseModel):
    title:str=Field(min_length=5,max_length=100)
    description:str=Field(min_length=30)
    item_type:str=Item_type.lost
    category:str
    location:str
    date_occurred:date
    date_occurred:date

    model_config=ConfigDict(from_attributes=True)
    
class ItemUpdate(BaseModel):
    title:Optional[str]=Field(min_length=5,max_length=100)
    description:Optional[str]=Field(min_length=30)
    item_type:Optional[str]=Item_type.lost
    category:Optional[str]=None
    location:Optional[str]=None
    date_occurred:Optional[date]=None
   
    
    model_config=ConfigDict(from_attributes=True)
    
class ItemResponse(BaseModel):
    id:int
    title:str=Field(min_length=5,max_length=100)
    description:str=Field(min_length=30)
    item_type:str
    category:str
    location:str
    date_occurred:Optional[date]=None
    image_id:Optional[int]=None
    created_at:datetime
    updated_at:datetime  
    created_by:int   
    
    model_config=ConfigDict(from_attributes=True)
    
class PaginationResponse(BaseModel):
    page:int
    limit:int
    total:int
    total_pages:int
    has_next:bool
    has_previous:bool
    items:List[ItemResponse]
    
    model_config=ConfigDict(from_attributes=True)