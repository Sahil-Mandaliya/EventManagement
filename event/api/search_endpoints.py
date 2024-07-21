from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
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
    try:
        events = search_events(name, event_date, location, db)
        return events
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    # Add rollback in exceptions
