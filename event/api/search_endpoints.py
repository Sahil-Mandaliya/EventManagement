from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from event.dto.event import EventDto
from event.service.event import search_events
from main_app.database import get_db
from sqlalchemy.orm import Session

search_router = APIRouter()

@search_router.get("/", response_model=List[EventDto])
def search_event_by_param(
        name: Optional[str] = Query(None, min_length=1, max_length=50),
        event_date: Optional[str] = None,
        location: Optional[str] = Query(None, min_length=1, max_length=50),
        db: Session = Depends(get_db)
    ):
    # Add validations
    return search_events(name, event_date, location, db)
    # Add rollback in exceptions
