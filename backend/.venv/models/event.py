from pydantic import BaseModel
from datetime import datetime
class Event(BaseModel):
    session_id : str
    event_type : str
    payload : dict
    timestamp :datetime

