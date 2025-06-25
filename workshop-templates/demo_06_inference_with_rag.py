import os

from dotenv import load_dotenv
from llama_stack_client import LlamaStackClient
from llama_stack_client.types.shared_params import UserMessage, Document, SystemMessage


load_dotenv()

vector_db_id = "dev_conf_cz_info"
# create llama stack client
client = LlamaStackClient(base_url=os.getenv("LLAMA_STACK_SERVER"))

def chat_with_rag_enabled_inference(query: str) -> str:
    # inference chat completion
    pass

if __name__ == "__main__":
    chat_with_rag_enabled_inference("Find talks by Abhishek Kumar")