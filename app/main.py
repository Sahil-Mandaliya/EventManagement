from fastapi import APIRouter
from app.admin.api import endpoints

api_router = APIRouter()
api_router.include_router(endpoints.router, prefix="/admin", tags=["admin"])