from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from event.models.event_registration import EventRegistration


def create_event_registration_to_db(event_data:EventRegistration, db: Session):
    try:
        db.add(event_data)
        db.commit()
        db.refresh(event_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise

    return event_data
