from fastapi import FastAPI
from app.core.config import settings

app=FastAPI(title=settings.app_name,
            debug=settings.debug,
            description="easily found your losts",
            version="1.0.0")


@app.get("/health",tags=["Health"])
def health_check():
    return {
        "status":"OK",
        "message":"Lost&Found Platform API is running"
    }