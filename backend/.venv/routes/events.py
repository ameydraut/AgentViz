
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