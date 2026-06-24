
from models.event import Event
from fastapi import APIRouter
router = APIRouter()
events=[]

@router.post("/events")
def create_event(event:Event):
    events.append(event.model_dump())
    return event

@router.get("/events")
def get_event():
    return events

@router.get("/sessions/{sessionId}/event")
def get_sessionEvents(sessionId:str):
    return [ 
        event
        for event in events
        if event["session_id"] == sessionId
        ]
@router.get("/session/{sessionId}/timelinedata")
def get_eventTimeLine(sessionId:str):
    session_events =[
        event
        for event in events
        if event["session_id"] == sessionId
    ] 
    return sorted(
        session_events,
        key=lambda event:event["timestamp"]
    )