import uuid

from llama_stack_client import LlamaStackClient, Agent
from dotenv import load_dotenv
import os

from llama_stack_client.types import UserMessage

load_dotenv()

# create llama stack cloient


def create_simple_agent_session(prefix):
   pass

def chat_with_simple_agent(session_id, query):
    pass


if __name__ == "__main__":
    print(chat_with_simple_agent(create_simple_agent_session("demo_agent_session"),
                          "Tell me about you and explain how you are different from simple chat completion"))
