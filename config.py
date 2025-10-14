
import os

class Config:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
    GOOGLE_MODEL = os.environ.get("GOOGLE_MODEL", "gemini-1.5")
    DEFAULT_TEMPERATURE = float(os.environ.get("GOOGLE_TEMP", 0.7))
    DEFAULT_MAX_TOKENS = int(os.environ.get("GOOGLE_MAX_TOKENS", 256))
    LOG_DIR = os.environ.get("LOG_DIR", "./data")
    CRISIS_KEYWORDS = [
        "kill myself", "i want to die", "suicid",
        "end my life", "hurt myself", "self-harm", "want to die"
    ]
