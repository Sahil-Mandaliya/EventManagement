
from typing import List
from pydantic import BaseModel

from event.dto.event import EventDto


class CreateEventResponseDto(BaseModel):
    event: EventDto


class DeleteEventResponse(BaseModel):
    message:str

class EventRegistrationResponse(BaseModel):
    message:str

