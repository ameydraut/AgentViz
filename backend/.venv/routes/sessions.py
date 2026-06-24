from fastapi import APIRouter
import uuid
router = APIRouter()
sessions=[]
@router.post("/sessions")
def create_session():
    session={
        "session_id":str(uuid.uuid4()),
        "status":"running"
    }

    sessions.append(session)
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

