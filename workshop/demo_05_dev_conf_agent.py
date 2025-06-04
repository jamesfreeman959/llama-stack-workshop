import os
import uuid

from dotenv import load_dotenv
from llama_stack_client import LlamaStackClient, Agent
from llama_stack_client.types import UserMessage
from llama_stack_client.types.agents.turn_create_params import ToolgroupAgentToolGroupWithArgs

load_dotenv()


def create_dev_conf_cz_agent_session(prefix: str):
    pass

def chat_with_dev_conf_cz_agent(session_id: str, user_message: str):
    pass

if __name__ == "__main__":
    user_message = "Find all LLama Stack talk in Dev Conf CZ with full details"
    session_id = create_dev_conf_cz_agent_session("demo_session")
    response = chat_with_dev_conf_cz_agent(session_id, user_message)
    print(f"\nUser Message: {user_message}")
    print(f"\nAgent Response: {response}")