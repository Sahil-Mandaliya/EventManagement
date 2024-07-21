
from datetime import datetime
from typing import List
from pydantic import BaseModel

from event.dto.event import EventDto, EventRegistration as EventRegistrationDto
from main_app.api import ApiResponse


class EventResponse(BaseModel):
    event: EventDto

class CreateEventResponse(ApiResponse):
    data: EventResponse

class UpdateEventResponse(ApiResponse):
    data: EventResponse

class DeleteEventResponse(ApiResponse):
    pass

class EventRegistrationResponse(ApiResponse):
    data: EventRegistrationDto

    class Config:
        arbitrary_types_allowed = True

