import uuid

from llama_stack_client import LlamaStackClient, Agent
from dotenv import load_dotenv
import os

from llama_stack_client.types import UserMessage

load_dotenv()


# create llama stack client
client = LlamaStackClient(base_url=os.getenv("LLAMA_STACK_SERVER"))

# create agent
agent = Agent(client=client,
              instructions="You are helpful assistant",
              model=os.getenv("INFERENCE_MODEL_ID"),
              )

def create_simple_agent_session(prefix):
    return agent.create_session(f"{prefix}_{uuid.uuid4()}")


def chat_with_simple_agent(session_id, query):
    response = agent.create_turn(
        session_id=session_id,
        messages=[
            UserMessage(role="user", content=query),
        ],
        stream=False,
    )
    return response.output_message.content


if __name__ == "__main__":
    user_message = "Tell me about you and explain how you are different from simple chat completion"
    session_id = create_simple_agent_session("demo_agent_session")
    response = chat_with_simple_agent(session_id, user_message)
    print(f"\nUser Message: {user_message}")
    print(f"\nAgent Response: {response}")
