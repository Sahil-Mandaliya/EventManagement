from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from main_app.database import Base
from main_app.models import TimeStampModel, SoftDeleteModel

class EventRegistration(TimeStampModel, SoftDeleteModel):
    __tablename__ = "event_registration"
    
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'), index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    registration_date = Column(DateTime)
    status = Column(Enum('Confirmed', 'Pending', 'Cancelled', name='registration_status'))
    number_of_tickets = Column(Integer, default=1)
    additional_notes = Column(String(500))

    event = relationship("Event", back_populates="event_registrations")