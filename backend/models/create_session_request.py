from pydantic import BaseModel
class createSessionRequest(BaseModel):
    user_query : str
    
