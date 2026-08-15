from app.schemas.item import ItemCreate,ItemUpdate
from sqlalchemy.orm import Session
from app.models.item import Items,Item_type
from fastapi import HTTPException,status

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

def get_all(db:Session):
    item=db.query(Items).all()
    return item

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