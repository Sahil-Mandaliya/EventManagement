from datetime import date, time, datetime
from typing import Optional
from pydantic import BaseModel

class EventDto(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    duration: Optional[float]
    location: str
    is_deleted: Optional[bool]

    class Config:
        orm_mode = True


class EventRegistrationDto(BaseModel):
    registration_id: int
    event: EventDto
    user_id: int
    registration_date: datetime
    status: str
    number_of_tickets: int
    additional_notes: Optional[str]

    class Config:
        arbitrary_types_allowed = True