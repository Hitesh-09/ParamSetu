import streamlit as st

from supabase_client import supabase

st.set_page_config(page_title="Admin Dashboard", layout="wide")

st.title("🧑‍💼 Admin Dashboard")

st.caption(
    "Loads users, policies, and claims **directly from Supabase** (same source as the rider app). "
    "You do **not** need the FastAPI server running for this dashboard."
)


@st.cache_data(ttl=30)
def load_users():
    return supabase.table("users").select("*").execute().data or []


@st.cache_data(ttl=30)
def load_policies():
    return supabase.table("policies").select("*").execute().data or []


@st.cache_data(ttl=30)
def load_claims():
    return supabase.table("claims").select("*").execute().data or []


def safe_load(label: str, loader):
    try:
        return loader()
    except Exception as e:
        st.error(f"Could not load **{label}** from Supabase: `{e}`")
        return []


if st.sidebar.button("Refresh data"):
    load_users.clear()
    load_policies.clear()
    load_claims.clear()
    st.rerun()

# ---------------- FETCH DATA ----------------
users = safe_load("users", load_users)
policies = safe_load("policies", load_policies)
claims = safe_load("claims", load_claims)

# ---------------- METRICS ----------------
st.subheader("📊 System Overview")

col1, col2, col3 = st.columns(3)

col1.metric("👥 Users", len(users))
col2.metric("📜 Policies", len(policies))
col3.metric("💰 Claims", len(claims))

st.markdown("---")

# ---------------- USERS ----------------
st.subheader("👤 Users")

if users:
    st.dataframe(users)
else:
    st.info("No users found")

st.markdown("---")

# ---------------- POLICIES ----------------
st.subheader("📜 Policies")

if policies:
    st.dataframe(policies)
else:
    st.info("No policies found")

st.markdown("---")

# ---------------- CLAIMS ----------------
st.subheader("💰 Claims")

if claims:
    for claim in claims:
        user_ref = claim.get("user_mobile") or claim.get("user_id") or "—"
        st.markdown(f"""
        **User:** {user_ref}  
        **Event:** {claim.get('event_type', '—')}  
        **Payout:** ₹{claim.get('payout_amount', '—')}  
        **Status:** {claim.get('status', '—')}  
        ---
        """)
else:
    st.info("No claims yet")
