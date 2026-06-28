from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import SQLModel, Field
from models.eventtypes import EventType


class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    session_id: str
    event_type: EventType
    payload: dict = Field(sa_column=Column(JSON))
    timestamp: datetime = Field(default_factory=datetime.now)