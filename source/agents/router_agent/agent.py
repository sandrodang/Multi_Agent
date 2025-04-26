from google.adk.agents import LlmAgent
from source.agents.greeting_agent.agent import greeting_agent
from source.agents.weather_agent.agent import weather_agent
from source.agents.sql_agent.agent import create_sql_agent
from config import Config

# Tạo Router Agent đồng bộ với sub-agent SQL bất đồng bộ
async def create_router_agent():
    sql_agent, exit_stack = await create_sql_agent()

    router_agent = LlmAgent(
        name="RouterAgent",
        model=Config.MODEL,
        description="Routes requests to GreetingAgent, WeatherAgent hoặc SQLAgent dựa trên nội dung.",
        instruction=(
            "If the user input is a greeting (hello, hi, good morning/afternoon/evening), "
            "route to 'GreetingAgent'. "
            "If it mentions weather or a location, route to 'WeatherAgent'. "
            "Otherwise, treat as a database query and route to 'SQLAgent'."
        ),
        sub_agents=[
            greeting_agent,
            weather_agent,
            sql_agent
        ]
    )

    return router_agent, exit_stack
