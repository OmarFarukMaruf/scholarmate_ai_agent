from google.adk.sessions import DatabaseSessionService
from scholarmate_agent.config.settings import DB_URL

def get_session_service() -> DatabaseSessionService:
    # Persistent conversation storage (short-term memory)
    return DatabaseSessionService(db_url=DB_URL)