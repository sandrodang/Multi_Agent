from google.adk.agents import LlmAgent

greeting_agent = LlmAgent(
    name="GreetingAgent",
    model="gemini-2.0-flash",
    description="Handles simple greetings like hello, hi, good morning, etc.",
    instruction=(
        "You are a friendly greeting agent. "
        "Respond appropriately when the user says hello, hi, good morning/afternoon/evening."
    ),
)
