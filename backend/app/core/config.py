from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    app_name:str="lost and founf platform"
    app_env:str="development"
    debug:bool=True
    
    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str="HS256"
    ACCESS_TIME_EXPIRE_TOKEN:int=30
    
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
settings=Settings()