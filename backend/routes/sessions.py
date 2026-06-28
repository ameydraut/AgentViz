from fastapi import APIRouter
from models.session import Session as SessionModel
from models.create_session_request import createSessionRequest
from datetime import datetime
import uuid
from database.database import get_db
from sqlmodel import select
from fastapi import Depends
from sqlmodel import Session
from models.event import Event
from models.eventtypes import EventType
router = APIRouter()
@router.post("/sessions")
def create_session(
    request:createSessionRequest,
    db:Session = Depends(get_db)
    ):
    session=SessionModel(
        session_id=str(uuid.uuid4()),
        status="running",
        user_query=request.user_query,
        created_at=datetime.now()
    )

    db.add(session)
    db.commit()
    db.refresh(session)
    return session

@router.get("/sessions")
def get_allSessions(db: Session =Depends(get_db)):
    sessions = db.exec(
        select(SessionModel)
    ).all()
    return sessions

@router.get("/sessions/{session_id}")
def get_session(sessionID: str, 
                db: Session = Depends(get_db)):
    session = db.exec(select(SessionModel).where(SessionModel.session_id == sessionID)).first()
    return session 

@router.get("/sessions/{sessionId}/graph")
def get_session_graph(sessionId:str, 
                      db : Session = Depends(get_db)):
    nodes = []
    edges = []

    events = db.exec(
        select(Event)
        .where(Event.session_id == sessionId)
        .order_by(Event.timestamp)
    ).all()
    size = len(events)-1

    for index,event in enumerate(events):
        node ={
            "id":str(index),
            "label" : event.event_type,
            "type": event.event_type,
            "timestamp":event.timestamp,
            "payload":event.payload
        }
        nodes.append(node)
        
        if index < size:
            edge={
            "source" : str(index),
            "target" : str(index+1)
            }
            edges.append(edge)

    return {
        "nodes":nodes,
        "edges":edges
    }

@router.get("/sessions/{sessionId}/summary")
def get_summary(sessionId:str,
                db:Session = Depends(get_db)):
    events = db.exec(
        select(Event)
        .where(Event.session_id == sessionId)
        .order_by(Event.timestamp)
    ).all()
    sessiondata = db.exec(
        select(SessionModel)
        .where(SessionModel.session_id == sessionId)
    ).first()
    
    if not sessiondata:
        return {
        "message": "Session not found"
    }

    if not events:
        return {
            "status": sessiondata.status,
            "user_query": sessiondata.user_query,
            "response": "",
            "duration_ms": 0,
            "total_events": 0,
            "tool_calls": 0,
            "llm_calls": 0,
            "tools_used": [],
            "first_event": None,
            "last_event": None
        }

    response= ""    
    total_events = 0
    tool_calls = 0
    llm_calls = 0
    tools_used = []
    first_event = events[0]
    last_event = events[-1]
    duration = last_event.timestamp-first_event.timestamp

    for event in events:
        total_events += 1

        if event.event_type == EventType.TOOL_CALL :
            tool_calls += 1
            tools_used.append(event.payload.get("tool"))
        elif event.event_type == EventType.LLM_CALL :
            llm_calls += 1
        elif event.event_type == EventType.FINAL_RESPONSE:
            response = event.payload.get("response","")
            
    return {
        "status": sessiondata.status,
        "user_query": sessiondata.user_query,
        "response":response,
        "duration_ms":int(duration.total_seconds() * 1000),
        "total_events":total_events,
        "tool_calls":tool_calls,
        "llm_calls": llm_calls,
        "tools_used": tools_used,
        "first_event" : first_event.event_type,
        "last_event":last_event.event_type
    }