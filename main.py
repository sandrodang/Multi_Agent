import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.genai import types
from source.agents.router_agent.agent import create_router_agent
from source.utils.env_loader import load_env

# Load environment variables
load_env()

async def main():
    print("Đang khởi tạo Router Agent...")
    router_agent, cleanup_stack = await create_router_agent()

    session_service = InMemorySessionService()
    artifact_service = InMemoryArtifactService()

    session = session_service.create_session(
        app_name="multi_agent_app",
        user_id="user123",
        session_id="session1"
    )

    runner = Runner(
        agent=router_agent,
        app_name="multi_agent_app",
        session_service=session_service,
        artifact_service=artifact_service,
    )

    print("Multi‑Agent ADK Demo (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        content = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )

        async for event in runner.run_async(
            user_id="user123",
            session_id="session1",
            new_message=content,
        ):
            if event.is_final_response():
                print("Agent:", event.content.parts[0].text)

    await cleanup_stack.aclose()

if __name__ == "__main__":
    asyncio.run(main())
# import os
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai import types
# from source.agents.router_agent.agent import router_agent
# from source.utils.env_loader import load_env

# # Load environment variables
# load_env()

# if __name__ == "__main__":

#     session_service = InMemorySessionService()
#     session = session_service.create_session(
#         app_name="multi_agent_app",
#         user_id="user123",
#         session_id="session1"
#     )
#     runner = Runner(
#         agent=router_agent,
#         app_name="multi_agent_app",
#         session_service=session_service
#     )

#     print("Multi‑Agent ADK Demo (type 'exit' to quit)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             break

#         # Wrap input in a Content object
#         content = types.Content(
#             role="user",
#             parts=[types.Part(text=user_input)]
#         )
#         # Pass Content to runner.run
#         events = runner.run(
#             user_id="user123",
#             session_id="session1",
#             new_message=content
#         )
#         for evt in events:
#             if evt.is_final_response():
#                 print("Agent:", evt.content.parts[0].text)
