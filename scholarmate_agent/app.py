from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.runners import Runner

from scholarmate_agent.agent import create_root_agent
from scholarmate_agent.services.sessions import get_session_service
from scholarmate_agent.services.memory import get_memory_service
from scholarmate_agent.config.settings import APP_NAME

def create_app() -> App:
    root_agent = create_root_agent()

    # Context compaction across events in a session
    compaction_config = EventsCompactionConfig(
        compaction_interval=4,  # summarize every 4 invocations
        overlap_size=1,         # one overlapping window for continuity
    )

    return App(
        name=APP_NAME,
        root_agent=root_agent,
        events_compaction_config=compaction_config,
    )

def create_runner() -> Runner:
    app = create_app()
    session_service = get_session_service()
    memory_service = get_memory_service()

    runner = Runner(
        app=app,
        session_service=session_service,
        memory_service=memory_service,
    )
    return runner