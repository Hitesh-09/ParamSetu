"""Render / local overrides via environment variables."""
import os

# FastAPI on Render (if you add HTTP calls from Streamlit). Override in Render → Environment.
BACKEND_URL = os.environ.get("BACKEND_URL", "https://paramsetu.onrender.com").rstrip("/")
