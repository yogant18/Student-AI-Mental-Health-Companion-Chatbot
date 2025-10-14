
import os, re, json
from datetime import datetime
from textblob import TextBlob
from config import Config

try:
    from transformers import pipeline
    _hf_sentiment = pipeline("sentiment-analysis")
except Exception:
    _hf_sentiment = None

TIPS_FILE = os.path.join(os.path.dirname(__file__), "templates", "tips.json")
LOG_DIR = Config.LOG_DIR
os.makedirs(LOG_DIR, exist_ok=True)

def get_sentiment(text: str):
    text = (text or "").strip()
    if not text:
        return {"label": "neutral", "score": 0.0}
    try:
        if _hf_sentiment:
            out = _hf_sentiment(text[:512])[0]
            return {"label": out.get("label","neutral").lower(), "score": float(out.get("score", 0.0))}
    except Exception:
        pass
    p = TextBlob(text).sentiment.polarity
    lbl = "positive" if p > 0.1 else "negative" if p < -0.1 else "neutral"
    return {"label": lbl, "score": abs(p)}

def detect_crisis(text: str):
    t = (text or "").lower()
    for kw in Config.CRISIS_KEYWORDS:
        if re.search(re.escape(kw), t):
            return True
    return False

def load_tips():
    try:
        with open(TIPS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return [
            "Box breathing: inhale 4s — hold 4s — exhale 4s — hold 4s.",
            "Grounding: name 5 things you can see, 4 you can touch, 3 you can hear."
        ]

def build_prompt(user_text: str, sentiment: dict, include_tip: bool = True):
    mood = sentiment.get("label","neutral")
    score = sentiment.get("score",0.0)
    tips = load_tips()
    tip_section = f"\nInclude one short relaxation tip from: {tips[:2]}" if include_tip else ""
    return f"""You are an empathetic student mental health assistant.
    User message: "{user_text}"
    Detected mood: {mood} (confidence {score:.2f}).
    Provide a short, kind, motivational reply (2–4 sentences){tip_section}.
    Avoid medical terms, and encourage seeking help if serious issues appear."""

def log_conversation(user_text, bot_text, sentiment):
    fname = os.path.join(LOG_DIR, f"conversation_{datetime.utcnow().strftime('%Y%m%dT%H%M%S')}.json")
    rec = {"time": datetime.utcnow().isoformat(), "user": user_text, "bot": bot_text, "sentiment": sentiment}
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=2)
