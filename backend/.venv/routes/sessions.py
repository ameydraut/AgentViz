from fastapi import APIRouter
from models.Session import Session
from models.create_session_request import createSessionRequest
from datetime import datetime
import uuid
router = APIRouter()
sessions=[]
@router.post("/sessions")
def create_session(request:createSessionRequest):
    session=Session(
        session_id=str(uuid.uuid4()),
        status="running",
        user_query=request.user_query,
        created_at=datetime.now()
    )

    sessions.append(session.model_dump())
    return session

@router.get("/sessions")
def get_allSessions():
    return sessions

@router.get("/sessions/{session_id}")
def get_session(sessionID: str):
    for session in sessions:
        if session["session_id"] == sessionID:
            return session
    return{
        "message": "Session not found"
    }


