"""
app.py

Main Streamlit application for the AI Interview Coach.
"""

import streamlit as st

try:
    from resume_parser import extract_resume_text
except ImportError:
    def extract_resume_text(uploaded_file):
        return "Resume parsing is temporarily disabled because the resume_parser module is unavailable."

from chatbot import get_ai_response
from memory import (
    initialize_memory,
    add_message,
    get_chat_history,
    clear_chat_history,
    display_chat_history,
)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide"
)

# -----------------------------
# Initialize Memory
# -----------------------------
initialize_memory()

# Store Resume Text
resume_text = ""

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("📌 AI Interview Coach")

    st.write("This chatbot simulates a professional HR interviewer.")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
- 🎤 HR Interview Simulation
- 🤖 AI-Powered Conversation
- 💬 Personalized Feedback
- 🧠 Chat Memory
- 📄 Resume Analysis
- ⚡ Google Gemini 2.5 Flash
- 🖥️ Streamlit Interface
""")

    st.markdown("---")

    st.subheader("🛠️ Technology Stack")

    st.markdown("""
- Python
- Streamlit
- Google Gemini API
- Prompt Engineering
- Session Memory
""")

    st.markdown("---")

    # -----------------------------
    # Resume Upload
    # -----------------------------
    st.subheader("📄 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_resume is not None:

        resume_text = extract_resume_text(uploaded_resume)

        st.success("✅ Resume uploaded successfully!")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        clear_chat_history()
        st.rerun()

    st.markdown("---")
    st.caption("Version 1.0")
    st.caption("Powered by Google Gemini 2.5 Flash")

# -----------------------------
# Main Title
# -----------------------------
st.title("🎯 AI Interview Coach")

st.markdown("""
### Practice Like a Real Job Interview

Welcome to the **AI Interview Coach**.

I will act as a professional **HR Interviewer**, ask one interview question at a time, evaluate your answers, and provide constructive feedback to help improve your interview performance.

👉 Upload your resume (optional) and type **"Start Interview"** below to begin your mock interview.
""")

# -----------------------------
# Display Previous Conversation
# -----------------------------
display_chat_history()

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input(
    "Type your answer or ask an interview-related question..."
)

if user_input:

    # Display User Message
    with st.chat_message("user"):
        st.write(user_input)

    # Include Resume Information
    if resume_text:

        user_input = f"""
Candidate Resume:

{resume_text}

Candidate Question:

{user_input}
"""

    # Generate AI Response
    with st.spinner("Generating response..."):

        ai_response = get_ai_response(
            user_input,
            get_chat_history()
        )

    # Display AI Response
    with st.chat_message("assistant"):
        st.write(ai_response)

    # Save Conversation
    add_message(
        user_input,
        ai_response
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "Developed by Andaluri Varshitha | AI Interview Coach | GenAI Assessment 2026"
)