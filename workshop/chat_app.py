import streamlit as st


# --- Sample functions ---
def chat_with_inference(user_message):
    return "not implemented"

def chat_with_agent(user_message):
    return "not implemented"

def chat_with_agent_with_web_search_tool(user_message):
    return "not implemented"

def dev_conf_agent(user_message):
    return "not implemented"

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
