from typing import List
from fastapi import APIRouter, Depends
from event.dto.event import EventDto
from event.service.event import get_all_events, get_event_by_id
from main_app.database import get_db
from sqlalchemy.orm import Session


api_router = APIRouter()

@api_router.get("/", response_model=List[EventDto])
def get_all_events_api(db: Session = Depends(get_db)):
    # Add validations
    return get_all_events(db)
    # Add rollback in exceptions

@api_router.get("/{event_id}", response_model=EventDto)
def get_event_by_id_api(event_id, db: Session = Depends(get_db)):
    # Add validations
    return get_event_by_id(event_id, db)
    # Add rollback in exceptions
