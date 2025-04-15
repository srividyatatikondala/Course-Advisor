import streamlit as st
from my_agent import ask_agent

# --- Page Config ---
st.set_page_config(page_title="🎓 AI Course Advisor", layout="centered", page_icon="🤖")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .main {
           
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .stTextInput>div>div>input {
            border: 2px solid #4CAF50;
            border-radius: 8px;
        }
        .chat-bubble-user {
            background-color: #d1e7dd;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 10px;
        }
        .chat-bubble-bot {
            background-color: #f8d7da;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title and description ---
st.title("🎓 AI-Powered Course Advisor Chatbot")
st.markdown("🤔 *Looking for learning courses? Ask away and get tailored recommendations from your personal course assistant!*")

# --- Session State for Chat History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Input Form ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Ask your question (e.g., Best Python courses for beginners)", key="user_input")
    submit = st.form_submit_button("🚀 Send")

# --- Handle Submission ---
if submit and user_input.strip():
    with st.spinner("🤖 Thinking..."):
        response = ask_agent(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Course Advisor", response))

# --- Display Chat History ---
st.markdown("<div class='main'>", unsafe_allow_html=True)
for speaker, message in reversed(st.session_state.chat_history):
    css_class = "chat-bubble-user" if speaker == "You" else "chat-bubble-bot"
    st.markdown(f"<div class='{css_class}'><strong>{speaker}:</strong> {message}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
