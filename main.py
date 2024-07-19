from fastapi import FastAPI
from user.api.endpoints import api_router as user_router
from event.api.endpoints import api_router as event_router
from event.api.public_endpoints import api_router as event_public_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"]) 
app.include_router(user_router, prefix="/role", tags=["role"]) 
app.include_router(event_router, prefix="/events", tags=["event"]) 
app.include_router(event_public_router, prefix="/events", tags=["event"]) 
