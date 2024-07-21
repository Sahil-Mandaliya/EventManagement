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
    event_id: int
    user_id: int
    full_name: str
    email: str
    phone: str
    number_of_tickets: Optional[str]
    additional_notes: Optional[str]