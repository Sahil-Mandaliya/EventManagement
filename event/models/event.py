# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from main_app.database import Base
from main_app.models import TimeStampModel, SoftDeleteModel


class Event(TimeStampModel, SoftDeleteModel):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(1000))
    location = Column(String(500), index=True, nullable=False)
    start_time = Column(DateTime, index=True)
    end_time = Column(DateTime)

    event_registrations = relationship("EventRegistration", back_populates="event")

    @property
    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 60

        return None
