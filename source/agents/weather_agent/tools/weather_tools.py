import os
import requests

def get_weather_info(city: str) -> dict:
    """
    Fetch current weather for `city` via OpenWeatherMap Current Weather Data API.

    Returns:
        dict: {"status": "success", "data": {...}} or
              {"status": "error", "error_message": "..."}
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return {"status": "error", "error_message": "OPENWEATHER_API_KEY not set."}

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        resp = requests.get(url, params=params, timeout=5)  # Requests HTTP lib :contentReference[oaicite:4]{index=4}
        resp.raise_for_status()
        return {"status": "success", "data": resp.json()}
    except requests.RequestException as e:
        return {"status": "error", "error_message": str(e)}
