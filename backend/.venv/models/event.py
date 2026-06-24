from datetime import datetime
from sqlmodel import SQLModel, Field
class Event(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    session_id : str
    event_type : str
    payload : str
    timestamp :datetime = Field(default_factory=datetime.now)

