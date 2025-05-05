from google.adk.agents import LlmAgent
from source.agents.weather_agent.tools import get_weather_info

weather_agent = LlmAgent(
    name="WeatherAgent",
    model="gemini-2.0-flash",
    description="Provides current weather info for a city.",
    instruction=(
        "When the user asks about the weather, call `get_weather_info(city)` "
        "and then summarize the JSON into a human-readable report."
    ),
    tools=[get_weather_info],  # ADK Function Tool pattern 
)
