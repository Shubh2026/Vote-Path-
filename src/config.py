"""
Application configuration — reads from environment variables only.
No secrets are ever hardcoded.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root explicitly
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


def get_gemini_api_key() -> str:
    """Return the Gemini API key from environment, or empty string."""
    return os.getenv("GEMINI_API_KEY", "")


# Gemini model identifiers
GEMINI_MODEL = "gemini-flash-latest"

# Rate-limiting defaults
RATE_LIMIT_MAX_CALLS = 10
RATE_LIMIT_WINDOW_SECONDS = 60

# App metadata
APP_TITLE = "BharatVote Guide"
APP_ICON = "🗳️"
APP_VERSION = "1.0.0"
