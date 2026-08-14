from app.schemas.user import UserCreate,UserUpdate
from fastapi import HTTPException,status 
from sqlalchemy.orm import Session
from app.models.usermodel import User
from app.schemas.password import PasswordChnage
from app.core.security import Hash

class Services():
    #@staticmethod
    def user_register(data:UserCreate,db:Session):
        existing=db.query(User).filter(User.email==data.email).first()
        hash_password=Hash.password_hash(data.password)
        if existing:
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="emaill already exist")
        
        user=User(
        full_name=data.full_name,
        password=hash_password,
        email=data.email,
        nick_name=data.nick_name
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    #@staticmethod
    
    def my_profile(user_id:int,db:Session):
        user=db.query(User).filter(User.id==user_id).first()
        return user
    
    def get_user_all(db:Session):
        user=db.query(User).all()
        return user
    
    def get_single(user_id:int,db:Session):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
        return user

    def update_user(user_id:int,current_user:User,data:UserUpdate,db:Session):
        if user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you can only update your own information")
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
        if data.full_name:
            user.full_name==data.full_name,
        if data.nick_name:
            user.nick_name=data.nick_name,
        if data.email:       
            user.email=data.email
        
        db.commit()
        db.refresh(user)
        return user
    
    def delete_user(user_id:int,current_user:User,db:Session):
        if user_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you can only delete your own information")
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
        db.delete(user)
        db.commit()
        return {
            "message":f"user with id {user_id} succesfuly deleted"
        }
    def change_password(user_id:int,data:PasswordChnage,db:Session):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="user not found")
        hash_password=Hash.verfy_password(data.current_password,user.password)
        if not hash_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong current password")
        updated=Hash.password_hash(data.new_password)
        
        user.password=updated
        db.commit()
        db.refresh(user)
        
        return {"password successful updated"}