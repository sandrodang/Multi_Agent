from google.adk.agents import LlmAgent
from config import Config

greeting_agent = LlmAgent(
    name="GreetingAgent",
    model=Config.MODEL,
    description="Handles simple greetings like hello, hi, good morning, etc.",
    instruction=(
        "You are a friendly greeting agent. "
        "Respond appropriately when the user says hello, hi, good morning/afternoon/evening."
    ),
)
