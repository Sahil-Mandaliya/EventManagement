from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from event.models.event import Event

def get_event_by_id_from_db(event_id, db: Session):
    event = db.query(Event).filter(Event.id == event_id, Event.is_deleted == False).first()
    if not event:
        return None
    return event

def get_all_events_from_db(db: Session):
    events = db.query(Event).filter(Event.is_deleted==False).all()
    return events


def create_event_to_db(event_data:Event, db: Session):
    try:
        db.add(event_data)
        db.commit()
        db.refresh(event_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise

    return event_data

def update_event_to_db(event_data:Event, db: Session):
    try:
        db.commit()
        db.refresh(event_data)
    except SQLAlchemyError as e:
        db.rollback()
        raise

    return event_data

def delete_event_from_db(event_id, db: Session):
    try:
        event  = get_event_by_id_from_db(event_id, db)
        if not event:
            return None

        event.is_deleted = True
        db.commit()
        db.refresh(event)
    except SQLAlchemyError as e:
        db.rollback()
        raise

    return

def search_events_in_db(filters: dict, db:Session):
    try: 
        events = []
        query = db.query(Event)
        query = query.filter(Event.is_deleted == False)
        for parameter in filters.keys():
            value = filters[parameter]
            if parameter == "name":
                query = query.filter(Event.name.ilike(f"%{value}%"))
            if parameter == "event_date":
                query = query.filter(func.date(Event.start_time)==value)
            if parameter == "location":
                query = query.filter(Event.location.ilike(f"%{value}%"))

        events = query.all()
        return events
    except SQLAlchemyError as e:
        db.rollback()
        raise

    return []