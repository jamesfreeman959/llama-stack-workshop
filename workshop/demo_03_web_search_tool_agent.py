import uuid

from llama_stack_client import LlamaStackClient, Agent
from dotenv import load_dotenv
import os

from llama_stack_client.lib.agents.client_tool import client_tool
from llama_stack_client.types.agents.turn_create_params import ToolConfig
from tavily import TavilyClient

from llama_stack_client.types import UserMessage

load_dotenv()

client = LlamaStackClient(base_url=os.getenv("LLAMA_STACK_SERVER"))


def travily_web_search(query: str):
    """
    Tool to perform web search for latest information. This tool returns array of search results consist of title, url, content.

    :param query: search query
    :return: array of search results, each result contains title, url, content, score.
    """
    pass


# create agent

def create_websearch_tool_agent_session(prefix: str):
    pass


def chat_with_websearch_tool_agent(session_id: str, user_message: str):
    pass


if __name__ == "__main__":
    user_message = "is Virat Kohli retired from test cricket?"
    session_id = create_websearch_tool_agent_session("demo_web_search_tool")
    response = chat_with_websearch_tool_agent(session_id,
                                              user_message)
    print(f"\nUser Message: {user_message}")
    print(f"\nAgent Response: {response}")
