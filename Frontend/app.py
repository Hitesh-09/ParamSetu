import streamlit as st
from datetime import datetime, timedelta
from supabase_client import supabase

st.set_page_config(page_title="ParamSetu", layout="centered")

# ---------------- SESSION SETUP ----------------
if "users" not in st.session_state:
    st.session_state.users = {}  # store users

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "event_triggered" not in st.session_state:
    st.session_state.event_triggered = False

if "event_history" not in st.session_state:
    st.session_state.event_history = {}

if "event_active" not in st.session_state:
    st.session_state.event_active = False

EVENT_COOLDOWN = timedelta(minutes=1)  # later this can be increased


def _claim_title(event_type: str) -> str:
    return (event_type or "Event").strip().title()


def fetch_latest_policy(user_mobile: str):
    policy_res = (
        supabase.table("policies")
        .select("*")
        .eq("user_mobile", user_mobile)
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )
    return policy_res.data[0] if policy_res.data else None


def fetch_claims(user_mobile: str):
    claims_res = (
        supabase.table("claims")
        .select("*")
        .eq("user_mobile", user_mobile)
        .order("created_at", desc=True)
        .execute()
    )
    return claims_res.data or []


def plan_label(policy: dict) -> str:
    key = (policy.get("premium"), policy.get("coverage_per_day"))
    names = {(20, 200): "Basic", (30, 400): "Standard", (50, 700): "Premium"}
    return names.get(key, "Your plan")


# ---------------- PLANS & DASHBOARD ----------------
if st.session_state.logged_in:

    # Fetch logged-in user from Supabase
    user_mobile = st.session_state.get("user_mobile")
    response = supabase.table("users").select("*").eq("mobile", user_mobile).execute()
    user = response.data[0] if response.data else None

    # Safety check
    if not user:
        st.error("User not found. Please login again.")
        st.session_state.logged_in = False
        st.rerun()

    policy = fetch_latest_policy(user_mobile)

    st.sidebar.title("🛵 ParamSetu")
    st.sidebar.markdown(f"**User:** {user['name']}")
    st.sidebar.markdown(f"📍 {user['location']}")
    st.sidebar.markdown(f"🚴 {user['platform']}")
    st.sidebar.divider()

    if st.sidebar.button("Logout"):
        st.session_state.update(
            {
                "logged_in": False,
                "event_triggered": False,
                "event_active": False,
            }
        )
        st.rerun()

    # If no policy in DB → only plan picker (no app navigation yet)
    if policy is None:
        st.title("📦 Choose Your Insurance Plan")

        col1, col2, col3 = st.columns(3)

        # ---- BASIC ----
        with col1:
            st.subheader("🟢 Basic")
            st.write("₹20/week")
            st.write("Coverage: ₹200/day")

            if st.button("Select Basic"):
                plan_data = {
                    "name": "Basic",
                    "premium": 20,
                    "coverage": 200,
                }

                supabase.table("policies").insert(
                    {
                        "user_mobile": st.session_state.user_mobile,
                        "premium": plan_data["premium"],
                        "coverage_per_day": plan_data["coverage"],
                        "risk_level": "medium",
                        "active": True,
                    }
                ).execute()

                st.success("Plan selected & saved!")
                st.rerun()

        # ---- STANDARD ----
        with col2:
            st.subheader("🟡 Standard ⭐")
            st.write("₹30/week")
            st.write("Coverage: ₹400/day")

            if st.button("Select Standard"):
                plan_data = {
                    "name": "Standard",
                    "premium": 30,
                    "coverage": 400,
                }

                supabase.table("policies").insert(
                    {
                        "user_mobile": st.session_state.user_mobile,
                        "premium": plan_data["premium"],
                        "coverage_per_day": plan_data["coverage"],
                        "risk_level": "medium",
                        "active": True,
                    }
                ).execute()

                st.success("Plan selected & saved!")
                st.rerun()

        # ---- PREMIUM ----
        with col3:
            st.subheader("🔴 Premium")
            st.write("₹50/week")
            st.write("Coverage: ₹700/day")

            if st.button("Select Premium"):
                plan_data = {
                    "name": "Premium",
                    "premium": 50,
                    "coverage": 700,
                }

                supabase.table("policies").insert(
                    {
                        "user_mobile": st.session_state.user_mobile,
                        "premium": plan_data["premium"],
                        "coverage_per_day": plan_data["coverage"],
                        "risk_level": "medium",
                        "active": True,
                    }
                ).execute()

                st.success("Plan selected & saved!")
                st.rerun()

        st.stop()

    page = st.sidebar.radio("Navigate", ["Dashboard", "My Policy", "Claims", "Admin"])

    claims = fetch_claims(user_mobile)

    # ---------------- NAVIGATED PAGES ----------------
    if page == "Dashboard":
        st.title("🏠 Rider Dashboard")

        st.markdown("### 👋 Welcome back!")
        st.divider()

        # ---- POLICY CARD ----
        st.markdown("### 📄 Your Policy")

        if policy:
            col1, col2, col3 = st.columns(3)
            col1.metric("Plan", "Active")
            col2.metric("Weekly Premium", f"₹{policy['premium']}")
            col3.metric("Coverage / Day", f"₹{policy['coverage_per_day']}")
        else:
            st.warning("No active policy found")

        st.divider()

        # ---- STATUS CARD ----
        st.markdown("### 📡 Live Status")

        if st.session_state.get("event_active"):
            st.error("🌧️ Heavy Rain Detected → Auto payout triggered")
        else:
            st.success("✅ No disruption detected. You are protected")

        st.divider()

        st.markdown("### ⚡ Demo — Simulate disruption")
        st.caption("Triggers a sample rain event and records a claim.")
        if st.button("Trigger Rain Event 🌧️"):
            event_name = "Heavy Rain"
            now = datetime.now()
            last_time = st.session_state.event_history.get(event_name)

            if last_time is None or (now - last_time) > EVENT_COOLDOWN:
                st.session_state.event_history[event_name] = now
                st.session_state.event_active = True
                st.session_state.event_triggered = True

                payout = policy["coverage_per_day"]

                supabase.table("claims").insert(
                    {
                        "user_mobile": st.session_state.user_mobile,
                        "event_type": event_name,
                        "payout_amount": payout,
                        "status": "triggered",
                    }
                ).execute()

                st.success(f"{event_name} detected — ₹{payout} credited.")
                st.rerun()
            else:
                remaining = EVENT_COOLDOWN - (now - last_time)
                st.warning(
                    f"{event_name} was processed recently. Try again in {remaining.seconds} seconds."
                )

        st.divider()

        # ---- RECENT CLAIMS ----
        st.markdown("### 🧾 Recent Claims")

        if not claims:
            st.info("No claims yet")
        else:
            for c in claims[:5]:
                st.markdown(
                    f"""
**{_claim_title(c.get('event_type', ''))}**  
💰 ₹{c.get('payout_amount', '—')}  
📌 Status: {c.get('status', '—')}
"""
                )
                st.divider()

        st.markdown("### 💰 Earnings Protected")

        total = sum(int(c["payout_amount"]) for c in claims)
        st.metric("Total Saved This Period", f"₹{total}")

    elif page == "My Policy":
        st.title("📄 My Policy")

        st.write(f"**Name:** {user['name']}")
        st.write(f"**Location:** {user['location']}")
        st.write(f"**Platform:** {user['platform']}")

        st.divider()

        if policy:
            st.write(f"**Plan:** {plan_label(policy)}")
            st.write(f"**Weekly Premium:** ₹{policy['premium']}")
            st.write(f"**Coverage per Day:** ₹{policy['coverage_per_day']}")
        else:
            st.warning("No active policy found")

        st.divider()

        st.subheader("📍 Risk Details")
        risk = policy.get("risk_level", "medium") if policy else "—"
        st.write(f"Risk Level: {risk}")
        st.write(f"Location: {user['location']}")
        st.write("Reason: Moderate rainfall and pollution in your city")

        st.success("Policy Active ✅")

    elif page == "Claims":
        st.title("🧾 Claims History")
        st.markdown("Full list of claims linked to your account.")

        st.divider()

        if not claims:
            st.info("No claims yet")
        else:
            for c in claims:
                st.markdown(
                    f"""
**{_claim_title(c.get('event_type', ''))}**  
💰 ₹{c.get('payout_amount', '—')}  
📌 Status: {c.get('status', '—')}
"""
                )
                st.divider()

    elif page == "Admin":
        st.title("🧑‍💻 Admin Dashboard")
        st.caption("Monitor users, policies, claims & payouts in real-time")

        st.divider()

        # ---- FETCH DATA ----
        users_res = supabase.table("users").select("*").execute()
        policies_res = supabase.table("policies").select("*").execute()
        claims_res = supabase.table("claims").select("*").execute()

        users = users_res.data or []
        policies = policies_res.data or []
        claims = claims_res.data or []

        st.markdown("### 📊 Key Metrics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("👥 Users", len(users))
        col2.metric("📄 Policies", len(policies))
        col3.metric("🧾 Claims", len(claims))

        total_payout = sum(int(c["payout_amount"]) for c in claims) if claims else 0
        col4.metric("💰 Total Payout", f"₹{total_payout}")

        st.divider()

        st.markdown("### 👥 Users Overview")

        if users:
            st.dataframe(users, use_container_width=True)
        else:
            st.info("No users registered yet")

        st.divider()

        st.markdown("### 📄 Active Policies")

        if policies:
            st.dataframe(policies, use_container_width=True)
        else:
            st.info("No policies created yet")

        st.divider()

        st.markdown("### 🧾 Claims Activity")

        if claims:
            st.dataframe(claims, use_container_width=True)
        else:
            st.info("No claims triggered yet")

    st.stop()

# ---------------- AUTH UI ----------------
st.title("🛵 ParamSetu - Rider App")

auth_mode = st.radio("Select Option", ["Sign In", "Sign Up"])

# ---------------- SIGN UP ----------------
if auth_mode == "Sign Up":
    st.subheader("🆕 Register")

    name = st.text_input("Full Name")
    mobile = st.text_input("Mobile Number")

    platform = st.selectbox(
        "Delivery Platform",
        ["Swiggy", "Zomato", "Uber Eats", "Zepto", "Dunzo"],
    )

    city = st.text_input("City / Working Location")
    password = st.text_input("Create Password", type="password")

    if st.button("Register"):
        # VALIDATIONS
        if len(mobile) != 10 or not mobile.isdigit():
            st.error("Mobile number must be exactly 10 digits")

        elif len(password) < 6:
            st.error("Password must be at least 6 characters")

        else:
            existing_user = supabase.table("users").select("*").eq("mobile", mobile).execute()

            if existing_user.data:
                st.error("User already exists")

            else:
                supabase.table("users").insert(
                    {
                        "name": name,
                        "mobile": mobile,
                        "password": password,
                        "platform": platform,
                        "location": city,
                    }
                ).execute()

                st.success("Registered successfully!")
                st.session_state.logged_in = True
                st.session_state.user_mobile = mobile
                st.rerun()

# ---------------- SIGN IN ----------------
else:
    st.subheader("🔐 Login")

    mobile = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Fetch user from Supabase
        response = supabase.table("users").select("*").eq("mobile", mobile).execute()

        if not response.data:
            st.error("User not found. Please sign up first.")

        else:
            user = response.data[0]

            if user["password"] != password:
                st.error("Incorrect password")

            else:
                st.success("Login successful!")
                st.session_state.logged_in = True
                st.session_state.user_mobile = mobile
                st.rerun()
