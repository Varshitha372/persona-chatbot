"""
memory.py

This module manages the chat history using Streamlit Session State.
It helps the chatbot remember the conversation during the current session.
"""

import streamlit as st


# -----------------------------
# Initialize Session Memory
# -----------------------------

def initialize_memory():

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "interview_mode" not in st.session_state:
        st.session_state.interview_mode = False

    if "resume_text" not in st.session_state:
        st.session_state.resume_text = ""


# -----------------------------
# Add Chat Message
# -----------------------------

def add_message(user_message, assistant_message):

    st.session_state.chat_history.append(
        {
            "user": user_message,
            "assistant": assistant_message
        }
    )


# -----------------------------
# Get Chat History
# -----------------------------

def get_chat_history():

    return st.session_state.chat_history


# -----------------------------
# Clear Chat
# -----------------------------

def clear_chat_history():

    st.session_state.chat_history = []

    st.session_state.interview_mode = False

    st.session_state.resume_text = ""


# -----------------------------
# Set Resume Text
# -----------------------------

def set_resume_text(resume_text):

    st.session_state.resume_text = resume_text


# -----------------------------
# Get Resume Text
# -----------------------------

def get_resume_text():

    return st.session_state.resume_text


# -----------------------------
# Start Interview
# -----------------------------

def start_interview():

    st.session_state.interview_mode = True


# -----------------------------
# Check Interview Mode
# -----------------------------

def is_interview_mode():

    return st.session_state.interview_mode


# -----------------------------
# Display Chat History
# -----------------------------

def display_chat_history():

    for chat in st.session_state.chat_history:

        with st.chat_message("user"):
            st.write(chat["user"])

        with st.chat_message("assistant"):
            st.write(chat["assistant"])