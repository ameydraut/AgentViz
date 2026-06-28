from datetime import datetime
from sqlmodel import SQLModel , Field
class Session(SQLModel, table = True):
    session_id:str=Field(primary_key=True)
    status:str
    user_query:str
    created_at:datetime