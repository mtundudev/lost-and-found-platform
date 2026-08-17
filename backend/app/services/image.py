from fastapi import File,UploadFile,HTTPException,status
import uuid
from pathlib import Path
from sqlalchemy.orm import Session
from app.models.item import Items
from app.models.image import Image

async def upload_image(item_id:int,current_user,db:Session,file:UploadFile=File(...)):
    item =db.query(Items).filter((Items.id == item_id)).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not found")
    if (item.created_by != current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=" only the owner can access")
   
    
    ALLOWED_MIME_TYPE={
        "image/jpeg",
        "image/png",
        "image/png"
    }
    ALLOWE_EXTENSION={
        ".png",".jpg","jpeg"
    }
    
    MAX_FILE_SIZE=5*1024*1024
    
    UPLOAD_DIR=Path("uploads/images")
    UPLOAD_DIR.mkdir(parents=True,exist_ok=True)
    
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,deteil="image/filename is required")
    
    extension=Path(file.filename).suffix.lower()
    if extension not in ALLOWE_EXTENSION:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="only JPG,JPEG.PNG are allowed")
    
    if file.content_type not in ALLOWED_MIME_TYPE:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="image type not allowed")
    
    new_filename=f"item_{uuid.uuid4()}{extension}"
    file_path=UPLOAD_DIR/new_filename
    
    with open(file_path,"wb") as buffer:
        buffer.write(await file.read())
    
    image=None
    if item.image_id:
        image=db.query(Image).filter(Image.id==item.image_id).first()
        
    if image:
        image.file_path=str(file_path),
        image.new_filename=new_filename,
        image.original_filename=file.filename,
        image.mime_type=file.content_type
     
        
    else:       
        image=Image(
            uploaded_by=current_user.id,
            original_filename=file.filename,
            new_filename=new_filename,
            file_path=str(file_path),
            mime_type=file.content_type
        ) 
        db.add(image)
        db.flush()
        item.image_id=image.id
   
    
    db.commit()
    db.refresh(image)
    
    
    return image

def item_image(item_id:int,db:Session):
    
    item=db.query(Items).filter(Items.id==item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not found")
    
    image=db.query(Image).filter(Image.id==item.image_id).first()
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item has no image")
    return image


def delete_image(item_id:int,current_user,db:Session):
    item=db.query(Items).filter(Items.id==item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item not found")
    if(item.created_by != current_user.id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="you not have action to perform this action")
    image=db.query(Image).filter(Image.id==item.image_id).first()
    
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="item has no image")
    
    db.delete(image)
    db.commit()
    return {"message":"item image delete succesfully"}