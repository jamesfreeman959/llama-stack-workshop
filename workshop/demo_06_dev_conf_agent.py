import os
import uuid

from dotenv import load_dotenv
from llama_stack_client import LlamaStackClient, Agent
from llama_stack_client.types import UserMessage
from llama_stack_client.types.agents.turn_create_params import ToolgroupAgentToolGroupWithArgs

load_dotenv()


def create_dev_conf_cz_agent_session(prefix: str):
    pass

def chat_with_dev_conf_cz_agent(session_id: str, query: str):
    pass

if __name__ == "__main__":
    chat_with_dev_conf_cz_agent(create_dev_conf_cz_agent_session("demo_session"), "Find all LLama Stack talk in Dev Conf CZ with full details")