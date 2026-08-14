from fastapi import APIRouter,Depends
from app.core.database import get_db
from app.services.user_services import Services
from app.schemas.user import UserCreate,UserUpdate,UserResponse
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.usermodel import User
from app.schemas.password import PasswordChnage

router= APIRouter(prefix="/Users",tags=["User managment"])


@router.get("/me",response_model=UserResponse)
def profile(current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    return Services.my_profile(user_id=current_user.id,db=db)

@router.get("/all",response_model=list[UserResponse])
def show_all(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return Services.get_user_all(db)

@router.get("/{user_id}",response_model=UserResponse)
def show(user_id:int,
         db:Session=Depends(get_db),
         current_user:User=Depends(get_current_user)):
    return Services.get_single(user_id,db)

@router.put("/change-password")
def update_password(data:PasswordChnage,
                    db:Session=Depends(get_db),
                    current_user:User=Depends(get_current_user)):
    return Services.change_password(user_id=current_user.id,data=data,db=db)

@router.put("/{user_id:int}",response_model=UserResponse)
def update(user_id,
           data:UserUpdate,
           db:Session=Depends(get_db),
           current_user:User=Depends(get_current_user)):
    return Services.update_user(user_id,current_user,data=data,db=db)


@router.delete("/{user_id}")
def delete(user_id:int,
           db:Session=Depends(get_db),
           current_user:User=Depends(get_current_user)):
    return Services.delete_user(user_id,current_user,db=db)
