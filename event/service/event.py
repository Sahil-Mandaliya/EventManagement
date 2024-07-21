from datetime import datetime
from typing import Optional
from dateutil.relativedelta import relativedelta
from fastapi import Depends
from sqlalchemy.orm import Session
from event.dto.event import EventDto
from event.dto.request import UpdateEventRequestDto
from event.repository.event import create_event_to_db, delete_event_from_db, get_all_events_from_db, get_event_by_id_from_db, search_events_in_db, update_event_to_db

from event.models.event import Event
from main_app.database import get_db
from main_app.utils.db_models import db_model_list_to_pydantic, db_model_to_pydantic


def create_event(event_dto:EventDto, db: Session):
    event_data = Event(
        name =event_dto.name,
        description =event_dto.description,
        location =event_dto.location,
        start_time = event_dto.start_time,
        end_time = event_dto.end_time
    )
    new_event = create_event_to_db(event_data=event_data, db=db)
    return new_event


def update_event(event_id, event_dto:UpdateEventRequestDto, db: Session):
    if not event_id:
        raise Exception("Event not found")
    
    event:Event = get_event_by_id(event_id, db)

    if event_dto.name:
        event.name = event_dto.name

    if event_dto.description:
        event.description = event_dto.description

    if event_dto.start_date and event_dto.start_time:
        event.start_time = event_dto.start_time

    if event_dto.end_date and event_dto.end_time:
        event.end_time = event_dto.end_time

    if event_dto.duration:
        event.end_time = event.start_time + relativedelta(minutes=event_dto.duration)

    if event_dto.location:
        event.location = event_dto.location

    if event.start_time > event.end_time:
        raise Exception("End time cannot be before start time")

    new_event = update_event_to_db(event_data=event, db=db)
    return new_event



def delete_event(event_id, db: Session):
    if not event_id:
        raise Exception("Event not found")
    
    delete_event_from_db(event_id=event_id, db=db)


def get_all_events(db: Session):
    db_events =  get_all_events_from_db(db)
    events = db_model_list_to_pydantic(db_events, EventDto)
    return events


def get_event_by_id(event_id, db: Session):
    db_event =  get_event_by_id_from_db(event_id, db)
    if not db_event:
        return None

    event = db_model_to_pydantic(db_event, EventDto)
    return event


def search_events(
    name: Optional[str],
    event_date: Optional[datetime],
    location: Optional[str],
    db: Session = Depends(get_db)
):
    db_events = []
    filters = {}
    if name:
        filters["name"]=name
    
    if event_date:
        filters["event_date"]=event_date
    
    if location:
        filters["location"]=location

    db_events = search_events_in_db(filters,db)
    events = db_model_list_to_pydantic(db_events, EventDto)
    return events