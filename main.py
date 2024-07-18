from fastapi import FastAPI
from user.api.endpoints import api_router as user_router

app = FastAPI()

from main_app.database import init_db

init_db()

app.include_router(user_router, prefix="/user", tags=["user"]) 
app.include_router(user_router, prefix="/role", tags=["role"]) 
