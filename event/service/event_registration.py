from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from event.dto.request import  EventRegistrationRequest
from event.dto.event import EventDto, EventRegistration as EventRegistrationDto

from event.repository.event_registration import create_event_registration_to_db

from event.models.event_registration import EventRegistration
from event.service.event import get_event_by_id
from main_app.utils.db_models import db_model_to_pydantic
from user.dto.user import UserDto
from user.repository.user.user import create_user, get_user_by_parameter


def add_event_bookings(event_id:int, event_dto:EventRegistrationRequest, db: Session):
    phone = event_dto.phone
    email = event_dto.email

    event = get_event_by_id(event_id, db)
    if not event:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event you are trying to book is no longer available")
    
    if event_dto.number_of_tickets > 10:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Maximum 10 tickets allowed per booking")
    
    user = None
    if phone:
        user = get_user_by_parameter("phone", phone, db)
    
    if not user and email:
        user =  get_user_by_parameter("email", email, db)

    if not user:
        user_dto = UserDto(
            full_name=event_dto.full_name,
            phone=event_dto.phone,
            email=event_dto.email,
            username=event_dto.email,
        )
        user  = create_user(user_dto=user_dto, db=db)

    event_data = EventRegistration(
        event_id = event_id,
        user_id = user.id,
        registration_date=func.now(),
        status = "Confirmed",
        number_of_tickets = event_dto.number_of_tickets,
        additional_notes = event_dto.additional_notes
    )

    new_event_registration = create_event_registration_to_db(event_data=event_data, db=db)

    return EventRegistrationDto(
        registration_id=new_event_registration.id,
        event=db_model_to_pydantic(new_event_registration.event, EventDto),
        user_id=new_event_registration.user_id,
        registration_date=new_event_registration.registration_date,
        status=new_event_registration.status,
        number_of_tickets=new_event_registration.number_of_tickets,
        additional_notes=new_event_registration.additional_notes,
    )
