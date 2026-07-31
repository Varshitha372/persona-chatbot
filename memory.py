"""
memory.py

This module manages the chat history using Streamlit Session State.
It helps the chatbot remember the conversation during the current session.
"""

import streamlit as st


def initialize_memory():
    """
    Initialize chat history when the application starts.
    """
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def add_message(user_message, assistant_message):
    """
    Save a user message and AI response to chat history.
    """
    st.session_state.chat_history.append(
        {
            "user": user_message,
            "assistant": assistant_message,
        }
    )


def get_chat_history():
    """
    Return the complete chat history.
    """
    return st.session_state.chat_history


def clear_chat_history():
    """
    Clear all previous conversations.
    """
    st.session_state.chat_history = []


def display_chat_history():
    """
    Display the complete conversation in the Streamlit interface.
    """
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat["user"])

        with st.chat_message("assistant"):
            st.write(chat["assistant"])