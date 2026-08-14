import bcrypt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from app.core.database import get_db
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from app.core.config import settings
from app.models import usermodel,revoked_token
from datetime import datetime,timedelta

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now() + timedelta(settings.ACCESS_TIME_EXPIRE_TOKEN)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    return token

def decode_token(token:str):
    payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
    email=payload.get("sub")
    if not email:
        raise JWTError("your token has valid information")
    return payload

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    revoked=db.query(revoked_token.RevokedToken).filter(revoked_token.RevokedToken.token==token).first()
    if revoked:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="please login again")
    
    payload=decode_token(token)
    email=payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validatecredentials")
    user=db.query(usermodel.User).filter(usermodel.User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user account not found. please  try to login again ")
    return user

class Hash():
    @staticmethod
    def password_hash(plain_password):
        plain_byte=plain_password.encode("utf-8")
        salt_byte=bcrypt.gensalt()
        hash=bcrypt.hashpw(plain_byte,salt_byte)
        return hash.decode("utf-8")
    @staticmethod
    def verfy_password(plain_passwod,hash_password):
        plain_byte=plain_passwod.encode("utf-8")
        hash_byte=hash_password.encode("utf-8")
        return bcrypt.checkpw(plain_byte,hash_byte)
    
        