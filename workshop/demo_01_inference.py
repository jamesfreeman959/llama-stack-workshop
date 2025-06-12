from llama_stack_client import *
import os
from dotenv import load_dotenv
from llama_stack_client.types.shared_params import UserMessage, SystemMessage

load_dotenv()

# create llama stack client
client = LlamaStackClient(base_url=os.getenv("LLAMA_STACK_SERVER"))

def chat_completion_with_inference(user_message: str):
    response = client.inference.chat_completion(
        model_id=os.getenv("INFERENCE_MODEL_ID"),
        messages=[
            UserMessage(role="user", content=user_message),
            SystemMessage(role="system", content="You are helpful assistant!"),
        ], stream=False
    )
    return response.completion_message.content


if __name__ == "__main__":
    user_message = "What is the capital of India?"
    response = chat_completion_with_inference(user_message)
    print("\nUser Message:", user_message)
    print("\nInference Response:", response)