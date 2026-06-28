from fastapi import FastAPI
from routes.sessions import router as sessions_router
from routes.events import router as events_router
from database.database import create_db_and_tables
app = FastAPI()
create_db_and_tables()
app.include_router(sessions_router)
app.include_router(events_router)