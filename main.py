from fastapi import FastAPI
from internal.api.endpoints import api_router as internal_router
from user.api.auth_endpoints import api_router as auth_router
from event.api.endpoints import api_router as event_router
from event.api.public_endpoints import api_router as event_public_router
from event.api.search_endpoints import search_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["internal"]) 
app.include_router(internal_router, prefix="/internal", tags=["internal"]) 
app.include_router(event_router, prefix="/events", tags=["event"]) 
app.include_router(event_public_router, prefix="/events", tags=["event"]) 
app.include_router(search_router, prefix="/search", tags=["search"])
