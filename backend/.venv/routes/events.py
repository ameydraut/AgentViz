from sqlmodel import SQLModel, select
from sqlmodel import Session
from fastapi import Depends
from models.event import Event
from fastapi import APIRouter
from database.database import get_session
router = APIRouter()
events=[]

@router.post("/events")
def create_event(event:Event,
                 db:Session =Depends(get_session)):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

@router.get("/events")
def get_event(db: Session =Depends(get_session)):
    events = db.exec(
        select(Event)
    ).all()
    return events

@router.get("/sessions/{sessionId}/event")
def get_sessionEvents(sessionId:str,
                      db: Session =Depends(get_session)):
    event = db.exec(select(Event).where(Event.session_id == sessionId)).all()
    return event

@router.get("/session/{sessionId}/timelinedata")
def get_eventTimeLine(sessionId:str,
                      db: Session =Depends(get_session)):
    session_events = db.exec(select(Event).where(Event.session_id == sessionId)).all()
    return sorted(
        session_events,
        key=lambda event:event.timestamp
    )