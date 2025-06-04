from llama_stack_client import *
import os
from dotenv import load_dotenv
from llama_stack_client.types.shared_params import UserMessage, SystemMessage

load_dotenv()

# create llama stack client


def chat_completion_with_inference(user_message: str):
    #chat completion
    pass


if __name__ == "__main__":
    user_message = "What is the capital of India?"
    response = chat_completion_with_inference(user_message)
    print("\nUser Message:", user_message)
    print("\nInference Response:", response)