import os
from dotenv import load_dotenv

# Load .env file (at project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

APP_NAME = "scholarship_finder_a2a_local"

# Gemini API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# SQLite file in project root
DB_URL = os.getenv("DB_URL", f"sqlite:///{os.path.join(BASE_DIR, 'scholarship_sessions.db')}")

USER_ID_NAMESPACE = "local_user"  # you can map real users later