from pydantic import BaseModel
from datetime import datetime
class Session(BaseModel):
    session_id:str
    status:str
    user_query:str
    created_at:datetime