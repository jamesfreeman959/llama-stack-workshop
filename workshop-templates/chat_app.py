import streamlit as st
from workshop.demo_01_inference import chat_completion_with_inference
from workshop.demo_02_agent import chat_with_simple_agent, create_simple_agent_session
from workshop.demo_03_web_search_tool_agent import chat_with_websearch_tool_agent, create_websearch_tool_agent_session
from workshop.demo_05_dev_conf_agent import chat_with_dev_conf_cz_agent, create_dev_conf_cz_agent_session



# --- Sample functions ---
def chat_with_inference(user_message):
    return chat_completion_with_inference(user_message)

def chat_with_agent(user_message):
    if "chat_with_agent" not in st.session_state:
        st.session_state["chat_with_agent"] = create_simple_agent_session("chat_with_agent")
    return chat_with_simple_agent(st.session_state["chat_with_agent"], query)


def chat_with_agent_with_web_search_tool(user_message):
    if "chat_with_web_search_tool_agent" not in st.session_state:
        st.session_state["chat_with_web_search_tool_agent"] = create_websearch_tool_agent_session(
            "chat_with_web_search_tool_agent")
    return chat_with_websearch_tool_agent(st.session_state["chat_with_web_search_tool_agent"], query)

def dev_conf_agent(user_message):
    if "dev_conf_agent_session_id" not in st.session_state:
        st.session_state["dev_conf_agent_session_id"] = create_dev_conf_cz_agent_session("dev_conf_agent_chat_app")
    return chat_with_dev_conf_cz_agent(st.session_state["dev_conf_agent_session_id"], query)

def chat_with_rag_inference(user_message):
    return "not implemented"


# --- Function map ---
FUNCTIONS = {
    "Simple Inference": chat_with_inference,
    "Rag Inference": chat_with_rag_inference,
    "Simple Agent": chat_with_agent,
    "Agent with Web Search": chat_with_agent_with_web_search_tool,
    "Chat With Dev Conf CZ Agent": dev_conf_agent,
}

# --- Page Setup ---
st.set_page_config(page_title="LLama Stack Chat", layout="centered")

# --- Session state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_function" not in st.session_state:
    st.session_state.selected_function = list(FUNCTIONS.keys())[0]
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# --- Sidebar: Function selection ---
with st.sidebar:
    st.header("⚙️ Choose Feature")
    selected_function = st.selectbox("LLama Stack Feature", list(FUNCTIONS.keys()), key="selected_function")

# --- Main Chat Display ---
st.title("💬 Chat with LLama Stack")

for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)

# --- Chat Input (Bottom) ---
query = st.chat_input("Type your message here...")

if query:
    # Display user message
    st.chat_message("user").markdown(query)
    st.session_state.chat_history.append(("user", query))

    # Get selected function
    func = FUNCTIONS[st.session_state.selected_function]

    # Call function
    response = func(query)

    # Display app response
    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append(("assistant", response))
