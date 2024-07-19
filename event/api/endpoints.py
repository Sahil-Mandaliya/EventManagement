from fastapi import APIRouter, Depends
from event.dto.event import EventDto
from event.dto.request import CreateEventRequestDto, EventRegistrationRequestDto, UpdateEventRequestDto, convert_create_event_request_to_event_dto
from event.dto.response import DeleteEventResponse, EventRegistrationResponse
from event.service.event import create_event, delete_event, update_event
from event.service.event_registration import add_event_bookings
from main_app.database import get_db
from sqlalchemy.orm import Session


api_router = APIRouter()

@api_router.post("/", response_model=EventDto)
def create_new_event_api(payload: CreateEventRequestDto, db: Session = Depends(get_db)):
    # Add validations
    event_dto = convert_create_event_request_to_event_dto(payload)
    return create_event(event_dto, db)
    # Add rollback in exceptions

@api_router.put("/{event_id}", response_model=EventDto)
def update_event_api(event_id: int, payload: UpdateEventRequestDto, db: Session = Depends(get_db)):
    # Add validations
    if not event_id:
        raise Exception("Event not found")

    payload.id = event_id
    return update_event(event_id, payload, db)
    # Add rollback in exceptions


@api_router.delete("/{event_id}", response_model=DeleteEventResponse)
def delete_event_api(event_id: int, db: Session = Depends(get_db)):
    # Add validations
    if not event_id:
        raise Exception("Event not found")

    delete_event(event_id, db)
    return DeleteEventResponse(message="Deleted successfully")
    # Add rollback in exceptions


@api_router.post("/{event_id}/register", response_model=EventRegistrationResponse)
def event_registration_api(event_id: int, payload: EventRegistrationRequestDto, db: Session = Depends(get_db)):
    # Add validations
    if not event_id:
        raise Exception("Event not found")

    payload.event_id=event_id
    add_event_bookings(event_id, payload, db)
    return EventRegistrationResponse(message="Registration successfull. please check your email and sms for the confirmation")
    # Add rollback in exceptions
