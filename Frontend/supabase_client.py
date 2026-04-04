import os

import streamlit as st
from supabase import create_client


def _supabase_credentials():
    s_url = s_key = None
    try:
        s_url = st.secrets["SUPABASE_URL"]
        s_key = st.secrets["SUPABASE_KEY"]
    except FileNotFoundError:
        pass
    except KeyError as e:
        raise RuntimeError(
            f"Missing secret {e!s}. Add SUPABASE_URL and SUPABASE_KEY to "
            ".streamlit/secrets.toml (local) or Streamlit Cloud → Settings → Secrets."
        ) from e

    url = os.environ.get("SUPABASE_URL") or s_url
    key = os.environ.get("SUPABASE_KEY") or s_key
    if url and key:
        return url, key

    raise RuntimeError(
        "No Supabase credentials found. Do one of the following:\n"
        "• Local: copy .streamlit/secrets.toml.example to .streamlit/secrets.toml and add your keys\n"
        "• Local: export SUPABASE_URL and SUPABASE_KEY in your shell\n"
        "• Streamlit Cloud: set the same keys under App settings → Secrets"
    )


SUPABASE_URL, SUPABASE_KEY = _supabase_credentials()
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
