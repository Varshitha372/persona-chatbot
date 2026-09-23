import os
import time

from dotenv import load_dotenv
from google import genai

from prompts import get_system_prompt


# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key) if api_key else None


def get_ai_response(
    user_message,
    chat_history,
    interview_mode=False,
    resume_text=""
):
    """
    Generate an AI response using Gemini.

    Modes:
    1. Normal Q&A
    2. Resume-based Q&A
    3. Interview mode
    """

    if client is None:
        return (
            "⚠️ Gemini API key is not configured. "
            "Please set GEMINI_API_KEY in your deployment environment."
        )

    # Select the correct system prompt
    system_prompt = get_system_prompt(
        interview_mode=interview_mode,
        resume_text=resume_text
    )

    conversation = system_prompt + "\n\n"

    # Add previous conversation
    for chat in chat_history:
        conversation += f"User: {chat['user']}\n"
        conversation += f"Ava: {chat['assistant']}\n\n"

    # Add current user message
    conversation += f"User: {user_message}\n"
    conversation += "Ava:"

    # Retry API call up to 3 times
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=conversation,
            )

            if response.text:
                return response.text

            return "I couldn't generate a response. Please try again."

        except Exception as e:

            if attempt < 2:
                time.sleep(5)

            else:
                return (
                    "⚠️ The Gemini AI service is currently unavailable.\n\n"
                    "Please wait a few moments and try again.\n\n"
                    f"Error Details: {e}"
                )