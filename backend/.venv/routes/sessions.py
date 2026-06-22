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
def get_sessions():
    return sessions