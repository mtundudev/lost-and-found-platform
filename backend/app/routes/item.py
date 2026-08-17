from fastapi import APIRouter,Query,Depends
from app.schemas.item import ItemUpdate,ItemCreate,ItemResponse,PaginationResponse
from app.services import item
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.usermodel import User
from typing import List

router=APIRouter(prefix="/Item",tags=["Items"])

@router.post("/new",response_model=ItemResponse)
def add(data:ItemCreate,db:Session=Depends(get_db),
        current_user:User=Depends(get_current_user)):
    return item.create_item(data,db,current_user)

@router.get("/",response_model=PaginationResponse)
def show_all(
    db:Session=Depends(get_db),location:str=None,status:str=None,
    category:str=None,page:int=Query(1,ge=1),
    limit:int=Query(10, ge=1, le=100),search:str=None,
    item_type:str=None,sort:str=None,order:str="asc"
     ):
    return item.get_all(db,category,location,status,
                        page,limit,search,
                        item_type,sort,order)

@router.get("/{item_id}",response_model=ItemResponse)
def  show_single(item_id:int,db:Session=Depends(get_db)):
    return item.get_by_id(item_id,db)

@router.put("/{item_id}",response_model=ItemResponse)
def update(item_id:int,data:ItemUpdate,db:Session=Depends(get_db),
           current_user:User=Depends(get_current_user)):
    return item.update_item(item_id,data,current_user,db)


@router.patch("/{item_id}status")
def status_update(item_id:int,item_status:str,
                  db:Session=Depends(get_db),
                  current_user:User=Depends(get_current_user)):
    return item.item_status(item_id,item_status,db,current_user)

@router.delete("/{item_id}")
def delete(item_id:int,db:Session=Depends(get_db),
            current_user:User=Depends(get_current_user)):
    return item.delete_item(item_id,current_user,db)