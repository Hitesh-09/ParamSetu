import os

import streamlit as st
from supabase import create_client


def _supabase_credentials():
    # Render / Docker / shell: set in Environment (recommended for deployed Streamlit)
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if url and key:
        return url, key

    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
    except FileNotFoundError:
        url = key = None
    except KeyError as e:
        raise RuntimeError(
            f"Missing secret {e!s}. Add SUPABASE_URL and SUPABASE_KEY to "
            ".streamlit/secrets.toml (local), Streamlit Cloud → Secrets, or Render → Environment."
        ) from e

    if url and key:
        return url, key

    raise RuntimeError(
        "No Supabase credentials found. Set **SUPABASE_URL** and **SUPABASE_KEY**:\n"
        "• **Render:** Web Service → Environment → add both variables (no quotes needed)\n"
        "• **Local:** `.streamlit/secrets.toml` or `export SUPABASE_URL=...` / `SUPABASE_KEY=...`\n"
        "• **Streamlit Cloud:** App → Settings → Secrets"
    )


SUPABASE_URL, SUPABASE_KEY = _supabase_credentials()
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
