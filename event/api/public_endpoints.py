# -*- coding: utf-8 -*-
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from event.dto.event import EventDto
from event.service.event import get_all_events, get_event_by_id
from main_app.database import get_db
from sqlalchemy.orm import Session


api_router = APIRouter()


@api_router.get("/", response_model=List[EventDto])
def get_all_events_api(db: Session = Depends(get_db)):
    # Add validations
    try:
        return get_all_events(db)
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    # Add rollback in exceptions


@api_router.get("/{event_id}", response_model=EventDto)
def get_event_by_id_api(event_id, db: Session = Depends(get_db)):
    # Add validations
    try:
        event = get_event_by_id(event_id, db)
        if not event:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Event is no longer available"
            )
        return event

    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    # Add rollback in exceptions
