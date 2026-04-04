🚀 Param Setu
Automated Parametric Insurance for Delivery Workers

Instant payouts. Zero claims. Powered by real-world data.








🌟 Overview

Param Setu is a next-generation parametric insurance platform designed to protect gig and delivery workers from income disruptions caused by environmental risks such as rain, heatwaves, and air pollution.

Unlike traditional insurance systems that rely on manual claim filing and lengthy verification processes, Param Setu leverages real-time data, automated triggers, and intelligent risk pricing to deliver instant payouts without human intervention.

🎯 Problem Statement

Delivery workers are highly vulnerable to:

🌧 Heavy rainfall
🌡 Extreme heat conditions
🌫 Poor air quality

These conditions directly impact their daily earnings.

However, existing insurance solutions are:

❌ Manual and slow
❌ Claim-heavy and complex
❌ Not designed for gig workers
💡 Solution

Param Setu introduces a fully automated parametric insurance system where:

User → Policy → Risk Engine → Event Detection → Automatic Claim → Instant Payout

✔ No claim filing
✔ No manual verification
✔ Instant financial protection

🔥 Key Features
⚡ Automated Event Engine
Continuously monitors real-world conditions
Uses OpenWeather APIs for:
Rainfall
Temperature
Air Quality (AQI)
Runs in the background to detect trigger events
💰 Instant Parametric Claims
Claims are triggered automatically
Fixed payout per event
No paperwork or delays
🌍 Multi-Trigger Support
🌧 Rain-based triggers
🌡 Heatwave triggers
🌫 Pollution (AQI) triggers
🧠 AI-Based Premium Calculation
Dynamic pricing using a rule-based risk engine
Factors:
Rainfall
Temperature
AQI
Outputs:
Risk Level (Low / Medium / High)
Weekly Premium
🛡 Fraud Prevention System
Prevents duplicate claims
Uses trusted external APIs for validation
Fully automated system eliminates manual manipulation
📱 Rider Dashboard (User App)
Simple login/register flow
Displays:
Premium
Risk level
Daily coverage
Shows automatic payouts in real-time
🧑‍💼 Admin Dashboard
Monitor users, policies, and claims
Track system activity
View triggered events and payouts
🧱 System Architecture
User → Policy Creation → Risk Engine → Event Engine → Claim Engine → Database
🛠️ Tech Stack
Category	Technology
Backend	FastAPI (Python)
Database	Supabase (PostgreSQL)
Frontend	Streamlit (User + Admin dashboards)
APIs	OpenWeather (Weather + AQI)
AI Logic	Rule-based risk engine
Automation	Background event engine
Testing	Postman
Version Control	GitHub
⚙️ How It Works
User registers on the platform
Policy is created with AI-calculated premium
System continuously monitors environmental data
If a trigger condition is met:
Claim is generated automatically
Payout is credited instantly
🛡 Policy Logic & Exclusions
Claims are triggered only when predefined thresholds are met
No duplicate payouts for the same event
Coverage is location-based
Only verified external data sources are used
🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/Hitesh-09/ParamSetu.git
cd ParamSetu
2️⃣ Setup Backend
cd Backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3️⃣ Configure Environment Variables

Create a .env file inside Backend/:

SUPABASE_URL=your_url
SUPABASE_KEY=your_key
WEATHER_API_KEY=your_api_key
4️⃣ Run Backend
python3 -m uvicorn app.main:app --reload
5️⃣ Run Rider App (Frontend)
streamlit run frontend/app.py
6️⃣ Run Admin Dashboard
streamlit run frontend/admin.py
📊 Demo Flow
Register a delivery worker
Create a policy (premium auto-calculated)
System monitors weather conditions
Trigger event occurs
Claim is generated automatically
Payout is displayed in dashboard
🏆 Innovation

Param Setu transforms insurance from:

Manual & Reactive → Automated & Proactive

By:

Eliminating claim friction
Enabling instant payouts
Using real-time environmental data
🌍 Impact
Protects gig workers’ income
Reduces claim processing time
Improves access to micro-insurance
Enables scalable, low-cost insurance models
🔮 Future Enhancements
📱 Mobile app (Flutter)
📍 GPS-based validation
🤖 ML-based risk scoring
🔔 Real-time alerts & notifications
🔗 Integration with delivery platforms
📌 Built With

FastAPI • Supabase • Streamlit • OpenWeather APIs • AI Risk Engine

👨‍💻 Team Param Setu

Building the future of automated, accessible insurance 🚀
