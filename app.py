"""
app.py

Main Streamlit application for the AI Interview Coach.
"""

import streamlit as st

from resume_parser import extract_resume_text, is_resume
from chatbot import get_ai_response

from memory import (
    initialize_memory,
    add_message,
    get_chat_history,
    clear_chat_history,
    display_chat_history,
    set_resume_text,
    get_resume_text,
    start_interview,
    is_interview_mode,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# INITIALIZE MEMORY
# ============================================================

initialize_memory()

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


# ============================================================
# DARK MODERN UI
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #070b14;
        color: #f5f7ff;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0b1120;
        border-right: 1px solid #1d2942;
    }

    /* Main content */
    .main {
        background-color: #070b14;
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff !important;
    }

    /* Normal text */
    p, li {
        color: #b8c2d6;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label {
        color: #c4ccdc;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        background-color: #0d1526;
        border: 1px solid #1d2a43;
        border-radius: 16px;
        margin-bottom: 12px;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        background-color: #0d1526;
        border: 1px solid #293957;
        border-radius: 16px;
    }

    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
        background-color: #0d1526 !important;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background-color: #111c32;
        color: #ffffff;
        border: 1px solid #2b3b5c;
        border-radius: 12px;
        font-weight: 600;
        min-height: 42px;
    }

    .stButton > button:hover {
        background-color: #1b2a48;
        border-color: #5576c5;
        color: #ffffff;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: #0d1526;
        border: 1px dashed #3a4c70;
        border-radius: 14px;
        padding: 8px;
    }

    /* Divider */
    hr {
        border-color: #1d2942;
    }

    /* Info / success / error boxes */
    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* Caption */
    .stCaption {
        color: #74829b !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎯 AI Interview Coach")

    st.caption(
        "Your AI-powered interview preparation assistant"
    )

    st.markdown("---")


    # --------------------------------------------------------
    # RESUME
    # --------------------------------------------------------

    st.subheader("📄 Resume")

    uploaded_resume = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"],
        key=f"resume_uploader_{st.session_state.uploader_key}",
        help="Upload a valid resume PDF. Resume upload is optional.",
    )

    if uploaded_resume is not None:

        resume_text = extract_resume_text(uploaded_resume)

        if is_resume(resume_text):

            set_resume_text(resume_text)

            st.success(
                "✅ Valid resume uploaded!"
            )

        else:

            # Remove any previously stored resume
            set_resume_text("")

            st.error(
                "❌ This PDF does not appear to be a valid resume."
            )

            st.caption(
                "Required: contact details, education, skills, "
                "and experience or projects."
            )

    elif not get_resume_text():

        st.info(
            "Resume upload is optional."
        )


    st.markdown("---")


    # --------------------------------------------------------
    # CURRENT MODE
    # --------------------------------------------------------

    st.subheader("🎤 Current Mode")

    if is_interview_mode():

        st.success(
            "🎤 Interview Mode ON"
        )

    else:

        st.info(
            "💬 Normal Q&A Mode"
        )


    st.markdown("---")


    # --------------------------------------------------------
    # FEATURES
    # --------------------------------------------------------

    st.subheader("✨ Features")

    st.markdown(
        """
        💬 **Normal AI Q&A**

        Ask questions normally before starting an interview.

        📄 **Resume Context**

        Ask questions based on your uploaded resume.

        🎤 **Mock Interview**

        Start a professional mock interview with AI.

        📝 **Interview Feedback**

        Get feedback after your interview answers.

        🧠 **Chat Memory**

        Maintain conversation context.
        """
    )


    st.markdown("---")


    # --------------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear Conversation"
    ):

        clear_chat_history()

        st.session_state.uploader_key += 1

        st.rerun()


    st.markdown("---")

    st.caption(
        "Version 2.0"
    )

    st.caption(
        "Powered by Google Gemini 2.5 Flash"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🎯 AI Interview Coach")

st.write(
    "Practice interviews, ask questions, and improve "
    "your interview skills with your personal AI coach."
)


if is_interview_mode():

    st.success(
        "🎤 Interview Mode Active"
    )

else:

    st.info(
        "💬 Normal Q&A Mode • Interview starts only when you "
        "say 'Start Interview'"
    )


# ============================================================
# WELCOME SECTION
# ============================================================

if not get_chat_history():

    st.subheader("👋 Welcome!")

    st.write(
        "You can ask me questions about interview preparation, "
        "HR, technical topics, programming, or career preparation."
    )

    st.write(
        "📄 Resume upload is optional."
    )

    st.write(
        "🎤 When you are ready, type **Start Interview** "
        "to begin your mock interview."
    )


# ============================================================
# QUICK START
# ============================================================

if not is_interview_mode():

    st.subheader("💡 Quick Start")

    col1, col2, col3 = st.columns(3)


    # HR Questions
    with col1:

        if st.button(
            "💼 HR Questions"
        ):

            question = (
                "Give me some common HR interview questions "
                "for a fresher."
            )

            ai_response = get_ai_response(
                question,
                get_chat_history(),
                interview_mode=False,
                resume_text=get_resume_text(),
            )

            add_message(
                question,
                ai_response,
            )

            st.rerun()


    # Python Questions
    with col2:

        if st.button(
            "🐍 Python Interview"
        ):

            question = (
                "Give me beginner-level Python interview "
                "questions with simple explanations."
            )

            ai_response = get_ai_response(
                question,
                get_chat_history(),
                interview_mode=False,
                resume_text=get_resume_text(),
            )

            add_message(
                question,
                ai_response,
            )

            st.rerun()


    # Start Interview
    with col3:

        if st.button(
            "🎤 Start Interview"
        ):

            start_interview()

            ai_response = get_ai_response(
                "Start the interview.",
                get_chat_history(),
                interview_mode=True,
                resume_text=get_resume_text(),
            )

            add_message(
                "Start Interview",
                ai_response,
            )

            st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

display_chat_history()


# ============================================================
# USER INPUT
# ============================================================

user_input = st.chat_input(
    "Ask anything or type 'Start Interview'..."
)


if user_input:

    user_input = user_input.strip()


    # --------------------------------------------------------
    # START INTERVIEW COMMAND
    # --------------------------------------------------------

    if user_input.lower() in [
        "start interview",
        "start the interview",
        "begin interview",
        "begin the interview",
    ]:

        start_interview()

        ai_response = get_ai_response(
            "Start the interview.",
            get_chat_history(),
            interview_mode=True,
            resume_text=get_resume_text(),
        )


    # --------------------------------------------------------
    # NORMAL QUESTION / INTERVIEW ANSWER
    # --------------------------------------------------------

    else:

        ai_response = get_ai_response(
            user_input,
            get_chat_history(),
            interview_mode=is_interview_mode(),
            resume_text=get_resume_text(),
        )


    # --------------------------------------------------------
    # SAVE MESSAGE
    # --------------------------------------------------------

    add_message(
        user_input,
        ai_response,
    )

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Developed by Andaluri Varshitha • AI Interview Coach"
)