from sqlalchemy import func
from sqlalchemy.orm import Session
from event.dto.request import  EventRegistrationRequestDto
from event.repository.event_registration import create_event_registration_to_db

from event.models.event_registration import EventRegistration
from user.dto.user import UserDto
from user.repository.user.user import create_user, get_user_by_parameter


def add_event_bookings(event_id:int, event_dto:EventRegistrationRequestDto, db: Session):
    phone = event_dto.phone
    email = event_dto.email
    user = None
    if phone:
        user = get_user_by_parameter("phone", phone, db)
    if email:
        user =  get_user_by_parameter("emial", email, db)

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

    new_event = create_event_registration_to_db(event_data=event_data, db=db)
    return new_event
