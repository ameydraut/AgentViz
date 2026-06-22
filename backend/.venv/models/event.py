from pydantic import BaseModel
class Event(BaseModel):
    session_id : str
    event_type : str
    payload : dict

