from fastapi import APIRouter,Depends,HTTPException,status
from app.models.usermodel import User
from sqlalchemy.orm import Session

from app.core.security import Hash,create_access_token

def login(db:Session,email:str,password:str):
      user=db.query(User).filter(User.email==email).first()
      if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong email")
      hash_password=Hash.verfy_password(password,user.password)
      if not hash_password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="check your password and try again")
      token=create_access_token({"sub":user.email})
      return{
            "access_token":token,
            "token_type":"Bearer"
      }
      
            
