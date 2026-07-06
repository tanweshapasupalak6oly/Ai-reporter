"""Configuration loader for AI Weekly Reporter."""

import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")


def validate():
    required = {
        'GEMINI_API_KEY': GEMINI_API_KEY,
        'EMAIL_TO': EMAIL_TO,
        'EMAIL_ADDRESS': EMAIL_ADDRESS,
        'EMAIL_APP_PASSWORD': EMAIL_APP_PASSWORD,
        'GOOGLE_SERVICE_ACCOUNT_JSON': GOOGLE_SERVICE_ACCOUNT_JSON,
    }
    missing = [k for k, v in required.items() if not v]
    if missing:
        raise RuntimeError(f"Missing required GitHub Secrets: {', '.join(missing)}")
