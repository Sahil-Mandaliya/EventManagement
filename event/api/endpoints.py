from fastapi import APIRouter, Depends, HTTPException, Request, status
from auth.decorator import has_roles
from event.dto.event import EventDto
from event.dto.request import CreateEventRequest, EventRegistrationRequest, UpdateEventRequestDto, convert_create_event_request_to_event_dto
from event.dto.response import EventResponse, CreateEventResponse,UpdateEventResponse, DeleteEventResponse, EventRegistrationResponse
from event.service.event import create_event, delete_event, update_event
from event.service.event_registration import add_event_bookings
from main_app.database import get_db
from sqlalchemy.orm import Session


api_router = APIRouter()

@api_router.post("/", response_model=CreateEventResponse)
@has_roles(["admin"])
def create_new_event_api(request: Request, payload: CreateEventRequest, db: Session = Depends(get_db)):
    try:
        event_dto = convert_create_event_request_to_event_dto(payload)
        event_dto = create_event(event_dto, db)
        return CreateEventResponse(
            status="Success",
            message="Event Created Successfully",
            data=EventResponse(
                event=event_dto
            )
        )
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")

@api_router.put("/{event_id}", response_model=UpdateEventResponse)
@has_roles(["admin"])
def update_event_api(request: Request, event_id: int, payload: UpdateEventRequestDto, db: Session = Depends(get_db)):
    # Add validations
    if not event_id:
        raise Exception("Event not found")

    payload.id = event_id
    try:
        updated_event = update_event(event_id, payload, db)
        return UpdateEventResponse(
            status="Success",
            message="Event Updated Successfully",
            data=EventResponse(
                event=updated_event
            )
        )
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    


@api_router.delete("/{event_id}", response_model=DeleteEventResponse)
@has_roles(["admin"])
def delete_event_api(request: Request, event_id: int, db: Session = Depends(get_db)):
    # Add validations
    if not event_id:
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event not found")

    try:
        delete_event(event_id, db)
        return DeleteEventResponse(status="Success", message="Deleted successfully")
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    
    # Add rollback in exceptions


@api_router.post("/{event_id}/register", response_model=EventRegistrationResponse)
def event_registration_api(event_id: int, payload: EventRegistrationRequest, db: Session = Depends(get_db)):
    # Add validations
    if not event_id:
        raise Exception("Event not found")
    try:
        payload.event_id=event_id
        new_event_registration = add_event_bookings(event_id, payload, db)
        return EventRegistrationResponse(
            status= "success",
            message="Registration successful",
            data = new_event_registration
        )
    except HTTPException as err:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong!")
    
    # Add rollback in exceptions
