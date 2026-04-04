import streamlit as st
from datetime import datetime, timedelta
from supabase_client import supabase

st.set_page_config(page_title="ParamSetu", layout="centered")

# ---------------- SESSION SETUP ----------------
if "users" not in st.session_state:
    st.session_state.users = {}  # store users

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "selected_plan" not in st.session_state:
    st.session_state.selected_plan = None

if "claims" not in st.session_state:
    st.session_state.claims = []

if "event_triggered" not in st.session_state:
    st.session_state.event_triggered = False

if "event_history" not in st.session_state:
    st.session_state.event_history = {}

EVENT_COOLDOWN = timedelta(minutes=1)  # later this can be increased

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

    page = st.sidebar.radio("Navigate", ["Dashboard", "My Policy", "Claims"])

    if st.sidebar.button("Logout"):
        st.session_state.update({
            "logged_in": False,
            "selected_plan": None,
            "claims": [],
            "event_triggered": False,
            "event_active": False
        })
        st.rerun()

    # If no plan selected → show plans first
    if st.session_state.selected_plan is None:

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
                    "coverage": 200
                }
                st.session_state.selected_plan = plan_data
                
                # Save to Supabase
                supabase.table("policies").insert({
                    "user_mobile": st.session_state.user_mobile,
                    "premium": plan_data["premium"],
                    "coverage_per_day": plan_data["coverage"],
                    "risk_level": "medium",
                    "active": True
                }).execute()
                
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
                    "coverage": 400
                }
                st.session_state.selected_plan = plan_data
                
                # Save to Supabase
                supabase.table("policies").insert({
                    "user_mobile": st.session_state.user_mobile,
                    "premium": plan_data["premium"],
                    "coverage_per_day": plan_data["coverage"],
                    "risk_level": "medium",
                    "active": True
                }).execute()
                
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
                    "coverage": 700
                }
                st.session_state.selected_plan = plan_data
                
                # Save to Supabase
                supabase.table("policies").insert({
                    "user_mobile": st.session_state.user_mobile,
                    "premium": plan_data["premium"],
                    "coverage_per_day": plan_data["coverage"],
                    "risk_level": "medium",
                    "active": True
                }).execute()
                
                st.success("Plan selected & saved!")
                st.rerun()

        st.stop()

    # ---------------- NAVIGATED PAGES ----------------
    plan = st.session_state.selected_plan

    if page == "Dashboard":
        st.title("🏠 Rider Dashboard")

        st.write(f"👋 Welcome, {user['name']}")
        st.write(f"📍 Location: {user['location']}")
        st.write(f"🚴 Platform: {user['platform']}")

        st.divider()

        col1, col2, col3 = st.columns(3)
        col1.metric("Plan", plan["name"])
        col2.metric("Weekly Premium", f"₹{plan['premium']}")
        col3.metric("Coverage / Day", f"₹{plan['coverage']}")

        st.divider()

        st.subheader("📡 Current Status")
        st.info("No disruption detected. You are covered ✅")

        st.divider()

        st.subheader("⚡ Simulate Disruption (Demo)")

        if st.button("Trigger Rain Event 🌧️"):
            event_name = "Heavy Rain"
            now = datetime.now()
            last_time = st.session_state.event_history.get(event_name)

            if last_time is None or (now - last_time) > EVENT_COOLDOWN:
                st.session_state.event_history[event_name] = now
                st.session_state.event_active = True
                st.session_state.event_triggered = True

                new_claim = {
                    "event": event_name,
                    "amount": plan["coverage"],
                    "status": "Paid",
                    "time": now.strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state.claims.append(new_claim)
                
                # Save claim to Supabase
                supabase.table("claims").insert({
                    "user_mobile": st.session_state.user_mobile,
                    "event_type": event_name,
                    "payout_amount": plan["coverage"],
                    "status": "triggered"
                }).execute()
                
                st.success(f"{event_name} detected → ₹{plan['coverage']} credited 💰")
            else:
                remaining = EVENT_COOLDOWN - (now - last_time)
                st.warning(f"{event_name} already processed. Try again in {remaining.seconds} sec")

        st.divider()

        st.subheader("💰 Earnings Protected")
        total = sum(c["amount"] for c in st.session_state.claims)
        st.metric("Total Saved", f"₹{total}")

    elif page == "My Policy":
        st.title("📄 My Policy")

        st.write(f"**Name:** {user['name']}")
        st.write(f"**Location:** {user['location']}")
        st.write(f"**Platform:** {user['platform']}")

        st.divider()

        st.write(f"**Plan:** {plan['name']}")
        st.write(f"**Weekly Premium:** ₹{plan['premium']}")
        st.write(f"**Coverage per Day:** ₹{plan['coverage']}")

        st.divider()

        st.subheader("📍 Risk Details")
        st.write(f"Risk Level: 🟡 Medium")
        st.write(f"Location: {user['location']}")
        st.write("Reason: Moderate rainfall and pollution in your city")

        st.success("Policy Active ✅")

    elif page == "Claims":
        st.title("🧾 Claims History")

        if len(st.session_state.claims) == 0:
            st.info("No claims yet")
        else:
            for claim in st.session_state.claims:
                st.write(f"🌧️ {claim['event']} → ₹{claim['amount']} → {claim['time']} → ✅ {claim['status']}")

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
        ["Swiggy", "Zomato", "Uber Eats", "Zepto", "Dunzo"]
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
                supabase.table("users").insert({
                    "name": name,
                    "mobile": mobile,
                    "password": password,
                    "platform": platform,
                    "location": city
                }).execute()

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