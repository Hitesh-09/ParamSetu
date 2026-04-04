from fastapi import APIRouter
from app.db import supabase
from app.services.weather_service import get_weather, get_aqi
from app.services.risk_engine import calculate_risk

router = APIRouter()

# Create policy
@router.post("/create")
def create_policy(policy: dict):
    user_id = policy["user_id"]

    # Fetch user details (location belongs to user)
    user = supabase.table("users") \
        .select("*") \
        .eq("id", user_id) \
        .single() \
        .execute()

    city = user.data["location"]

    weather = get_weather(city)
    rainfall = weather["rainfall"]
    temp = weather["temperature"]

    # For AQI we need lat/lon (mocked for now)
    lat, lon = 19.0760, 72.8777
    aqi = get_aqi(lat, lon)

    risk_data = calculate_risk(city, rainfall, temp, aqi)

    policy_data = {
        "user_id": user_id,
        "premium": risk_data["premium"],
        "coverage_per_day": 400,
        "risk_level": risk_data["risk"]
    }

    response = supabase.table("policies").insert(policy_data).execute()
    return response.data


# List all policies (must be registered before /{user_id} so "list" is not captured as an id)
@router.get("/")
def get_all_policies():
    response = supabase.table("policies").select("*").execute()
    return response.data


# Get policies for a user
@router.get("/{user_id}")
def get_user_policies(user_id: str):
    response = supabase.table("policies").select("*").eq("user_id", user_id).execute()
    return response.data