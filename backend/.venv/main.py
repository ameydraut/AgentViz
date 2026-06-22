from fastapi import FastAPI
from routes.sessions import router as sessions_router
from routes.events import router as events_router
app = FastAPI()
app.include_router(sessions_router)
app.include_router(events_router)