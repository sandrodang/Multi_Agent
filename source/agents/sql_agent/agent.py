from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import litellm 

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
litellm._turn_on_debug()
from litellm import completion
from litellm.llms.ollama.completion import transformation
from google.genai import types
# Override function gốc


# Hàm async lấy toolset từ MCP server
async def get_sql_tools():
    params = SseServerParams(
        url="http://localhost:8000/sse",
        headers={},
    )
    tools, exit_stack = await MCPToolset.from_server(connection_params=params)
    return tools, exit_stack


async def create_sql_agent():
    tools, exit_stack = await get_sql_tools()
    agent = LlmAgent(
        name="SQLAgent",

        model=LiteLlm(
            model= "openai/qwen2.5",
        ),
        instruction=(
            "Bạn là một agent kết nối đến PostgreSQL qua NL2SQL tool."
            "Chuyển câu hỏi tiếng Việt hoặc tiếng Anh thành SQL và thực thi nó."
        ),
        tools=tools,
        generate_content_config = types.GenerateContentConfig(
            max_output_tokens=1000,
            temperature=0,
        ),
    )
    return agent, exit_stack

# Tạo agent, trả về cả agent và exit_stack để cleanup sau này
# async def create_sql_agent():
#     tools, exit_stack = await get_sql_tools()
#     agent = LlmAgent(
#         name="SQLAgent",
#         model="gemini-2.0-flash",
#         instruction=(
#             "Bạn là một agent kết nối đến PostgreSQL qua NL2SQL tool. "
#             "Chuyển câu hỏi tiếng Việt hoặc tiếng Anh thành SQL và thực thi nó."
#         ),
#         tools=tools,
#     )
#     return agent, exit_stack
