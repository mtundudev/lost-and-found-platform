from fastapi import APIRouter,Depends,File,UploadFile
from app.core.database import get_db
from app.services import image
from sqlalchemy.orm import Session
from app.models.usermodel import User
from app.core.security import get_current_user

router=APIRouter(prefix="/item",tags=["Image"])

@router.post("/{item_id}/image")
async def upload_item(item_id:int,
                current_user:User=Depends(get_current_user),
                db:Session=Depends(get_db),file:UploadFile=File(...)):
    return await image.upload_image(item_id,current_user,db,file)

@router.get("{item_id}/image")
def upload_item(item_id:int,
                current_user:User=Depends(get_current_user),
                db:Session=Depends(get_db)):
    return image.item_image(item_id,db)

@router.delete("{item_image}/image")
def upload_item(item_id:int,
                current_user:User=Depends(get_current_user),
                db:Session=Depends(get_db)):
    return image.delete_image(item_id,current_user,db)