import streamlit as st
from my_agent import ask_agent

# Update the page config with a more focused title
st.set_page_config(page_title="AI Course Advisor", layout="centered")

# Updated page title and intro
st.title("🎓 AI-Powered Course Advisor Chatbot")
st.write("Looking for  Learning courses? Ask away and get tailored recommendations!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask your question (e.g., Best Python courses for beginners)", key="user_input")
    submit = st.form_submit_button("Send")

if submit and user_input.strip():
    with st.spinner("Thinking..."):
        response = ask_agent(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Course Advisor", response))

for speaker, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{speaker}:** {message}")
