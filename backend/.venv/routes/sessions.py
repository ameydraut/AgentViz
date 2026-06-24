from fastapi import APIRouter
from models.session import Session as SessionModel
from models.create_session_request import createSessionRequest
from datetime import datetime
import uuid
from database.database import get_session
from sqlmodel import select
from fastapi import Depends
from sqlmodel import Session
router = APIRouter()
@router.post("/sessions")
def create_session(
    request:createSessionRequest,
    db:Session = Depends(get_session)
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
def get_allSessions(db: Session =Depends(get_session)):
    sessions = db.exec(
        select(SessionModel)
    ).all()
    return sessions

@router.get("/sessions/{session_id}")
def get_session(sessionID: str, 
                db: Session = Depends(get_session)):
    session = db.exec(select(SessionModel).where(SessionModel.session_id == sessionID)).first()
    return session 
    


