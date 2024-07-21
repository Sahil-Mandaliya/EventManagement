# -*- coding: utf-8 -*-
from typing import List, Optional
from datetime import datetime, date, time
from dateutil.relativedelta import relativedelta
from pydantic import BaseModel
from main_app.api import ApiResponse

from event.dto.event import EventDto
from user.dto.user import RoleDto


class CreateEventRequest(BaseModel):
    name: str
    description: Optional[str]
    start_date: Optional[date]
    start_time: Optional[time]
    duration: Optional[float]
    end_date: Optional[date]
    end_time: Optional[time]
    location: str


def convert_create_event_request_to_event_dto(request_dto: CreateEventRequest):
    start_date = request_dto.start_date
    start_time = request_dto.start_time
    end_date = request_dto.end_date
    end_time = request_dto.end_time
    duration = request_dto.duration

    start_date_time = datetime.combine(start_date, start_time)
    if end_date and end_time:
        end_date_time = datetime.combine(end_date, end_time)
        duration = (end_date_time - start_date_time).total_seconds() / 60
    elif duration:
        end_date_time = start_date_time + relativedelta(minutes=duration)
    else:
        end_date_time = start_date_time + relativedelta(minutes=30)
        duration = (end_date_time - start_date_time).total_seconds() / 60

    return EventDto(
        name=request_dto.name,
        description=request_dto.description,
        start_time=start_date_time,
        end_time=end_date_time,
        duration=duration,
        location=request_dto.location,
    )


class UpdateEventRequestDto(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    start_date: Optional[date]
    start_time: Optional[time]
    duration: Optional[float]
    end_date: Optional[date]
    end_time: Optional[time]
    location: Optional[str]


class EventRegistrationRequest(BaseModel):
    event_id: Optional[int]
    full_name: str
    email: str
    phone: str
    number_of_tickets: Optional[int]
    additional_notes: Optional[str]
