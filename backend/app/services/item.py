from app.schemas.item import ItemCreate,ItemUpdate
from sqlalchemy.orm import Session
from app.models.item import Items,Item_type
from fastapi import HTTPException,status,Query
from sqlalchemy import or_,asc,desc
import math

def create_item(data:ItemCreate,db:Session,current_user):
    item=Items(
        title=data.title,
        category=data.category,
        description=data.description,
        location=data.location,
        item_type=data.item_type,
        image=data.image,
        date_occurred=data.date_occurred,
        created_by=current_user.id
    )
    if data.item_type not in Item_type:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,detail="item type should either lost or found")
    db.add(item)
    db.commit()
    db.refresh(item)
    
    return item

def get_all(
    db:Session,
    category:str=None,
    location:str=None,status:str=None,
    page:int=Query(1, ge=1),limit:int=Query(10,ge=1 ,le=100),
    search:str=None,item_type:str=None,
    sort:str=None,order:str="asc"
    ):
    item=db.query(Items)
    if search:
        item=item.filter(or_(
            Items.title.ilike(f"%{search}%"),
            Items.description.ilike(f"%{search}%"),
            Items.location.ilike(f"%{search}%"),
        ))
    if item_type:
        if (item_type not in [e.value for e in Item_type]):
            raise HTTPException(status_code=400,detail="item type shoul lost or found")
        item=item.filter(Items.item_type==item_type)
    if category:
           item=item.filter(Items.category==category) 
    if location:
        item=item.filter(Items.location.ilike(f"%{location}%"))  
    if status:
        item=item.filter(Items.status==status)         
    if sort:
        if sort=="title":
            item=item.order_by(asc(Items.title))
        else:
            item=item.order_by(desc(Items.title))  
    elif sort=="created_at":
        if sort=="asc":
            item=item.order_by(asc(Items.created_at))
        else:
            item=item.order_by(desc(Items.created_at))     
    else:
        item=item.order_by(desc(Items.created_at)) 
        
    total=item.count()    
    total_pages=math.ceil(total / limit)    
    skip=(page-1)*limit
    item= item.offset(skip).limit(limit).all()
    
    return{
            "page":page,
            "limit":limit,
            "total":total,
            "total_pages":total_pages,
            "has_next":page < total_pages,
            "has_previous": page >1,
            "items":item
        }
    

def get_by_id(item_id:int,db:Session):
    item=db.query(Items).filter(Items.id==item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="no any item oresent")
    return item

def update_item(item_id:int,data:ItemUpdate,current_user,db:Session):
    item=db.query(Items).filter(Items.id==item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not found")
    
    if(item.created_by != current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" you not have action to perform these")
    if data.title:
        item.title=data.title
    if data.description:    
        item.description=data.description
    if data.item_type:    
        item.item_type=data.item_type
    if data.image:    
        item.image=data.image
    if data.location:    
        item.location=data.location
    if data.category:    
        item.category=data.category
    if data.date_occurred:    
        item.date_occurred=data.date_occurred
    
    db.commit()
    db.refresh(item)
    return item

def delete_item(item_id:int,current_user,db:Session):
    item=db.query(Items).filter(Items.id==item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not found")
    if(item.created_by != current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" you not have action to perform these")
    db.delete(item)
    db.commit()
    
    return {
        "message":"item deleted successful"
    }