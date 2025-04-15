# 🎓 AI-Powered Course Advisor Chatbot

This is an AI-powered chatbot built using **Streamlit** that helps users discover personalized learning courses based on their interests. The chatbot provides intelligent responses using a custom agent, making it easier for learners to find the right resources for their journey.

## 🔍 Overview

The chatbot allows users to ask questions like “Best Python courses for beginners” and get tailored recommendations. It maintains a persistent chat history using Streamlit's session state and presents the conversation in a clean, readable format.

## 🧠 How It Works

- The main logic resides in the `ask_agent()` function located in `my_agent.py`.
- Users type their questions into a form built using Streamlit.
- The input is passed to `ask_agent()` which returns a response.
- Chat history is managed using `st.session_state.chat_history`.
- The app UI is defined in `app.py` and designed for a smooth user experience.

## 🖥️ Tech Stack

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- Custom AI agent logic (can be enhanced with GPT, Cohere, etc.)

## 📂 Project Structure
├── app.py               # Streamlit application
├── my_agent.py          # Core logic to generate responses
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
## 💡 Customization Ideas

Here are some ways you can extend and enhance the chatbot:

- 🔁 **Integrate GPT-4 or other LLMs**: Replace `ask_agent()` with OpenAI’s GPT-4 or Cohere for more intelligent responses.
- 🧠 **Connect to Real Course APIs**: Fetch real-time course data from platforms like [Coursera](https://www.coursera.org/), [Udemy](https://www.udemy.com/), or [edX](https://www.edx.org/) using their APIs.
- 🌍 **Add Multi-language Support**: Enable the chatbot to answer questions in different languages using translation APIs.
- 🎯 **Add Filters**: Allow users to filter results by cost (free/paid), level (beginner/intermediate/advanced), or duration.
- 🧾 **Database Integration**: Store chat logs or course selections in a database like Firebase, MongoDB, or SQLite.
- 💻 **Deploy on Cloud**: Host it on [Streamlit Cloud](https://streamlit.io/cloud), [Render](https://render.com/), or [Hugging Face Spaces](https://huggingface.co/spaces).


