from google.adk.agents import LlmAgent
from source.agents.greeting_agent.agent import greeting_agent
from source.agents.weather_agent.agent import weather_agent
from config import Config
router_agent = LlmAgent(
    name="RouterAgent",
    model=Config.MODEL,
    description="Routes greeting vs. weather requests to the right agent.",
    instruction=(
        "If input is a greeting, transfer to 'GreetingAgent'. "
        "If it mentions 'weather' or a city name, transfer to 'WeatherAgent'."
    ),
    sub_agents=[greeting_agent, weather_agent],
)
