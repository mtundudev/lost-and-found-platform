from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from fastapi import APIRouter,Depends,HTTPException,status
from app.services import auth,user_services
from app.schemas.user import UserResponse,UserCreate
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token
from datetime import datetime,timezone
from app.models.revoked_token import RevokedToken

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

router=APIRouter(tags=["Auth"])

@router.post("/create",response_model=UserResponse)
def register(data:UserCreate,db:Session=Depends(get_db)):
    return user_services.Services.user_register(data,db) 

@router.post("/login")
def login_user(db:Session=Depends(get_db),data:OAuth2PasswordRequestForm=Depends()):
    return auth.login(db,data.username,data.password)

@router.post("/logout")
def logout_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    revoked=db.query(RevokedToken).filter(RevokedToken.token==token).first()
    if revoked:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="already logout")
    payload=decode_token(token)
    expires_at=datetime.fromtimestamp(payload["exp"])
    revoked=RevokedToken(token=token,expire_at=expires_at)
    db.add(revoked)
    db.commit()
    db.refresh(revoked)
    return {
        "massage":"Logout succesful",
        "token":token
    }