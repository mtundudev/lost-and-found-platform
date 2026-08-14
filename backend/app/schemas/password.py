from pydantic import BaseModel

class PasswordChnage(BaseModel):
    current_password:str
    new_password:str
    
    