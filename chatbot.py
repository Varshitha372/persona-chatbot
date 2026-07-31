import os
import time
from dotenv import load_dotenv
from google import genai
from prompts import HR_SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Client only if an API key is available
client = genai.Client(api_key=api_key) if api_key else None


def get_ai_response(user_message, chat_history):
    """
    Generate AI response using Gemini.
    """

    if client is None:
        return (
            "⚠️ Gemini API key is not configured. "
            "Please set GEMINI_API_KEY in your deployment environment."
        )

    conversation = HR_SYSTEM_PROMPT + "\n\n"

    # Add previous conversation
    for chat in chat_history:
        conversation += f"Candidate: {chat['user']}\n"
        conversation += f"HR Interviewer: {chat['assistant']}\n"

    # Add current user message
    conversation += f"Candidate: {user_message}\n"
    conversation += "HR Interviewer:"

    # Retry API call up to 3 times
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=conversation,
            )

            return response.text

        except Exception as e:
            if attempt < 2:
                # Wait 5 seconds before retrying
                time.sleep(5)
            else:
                return (
                    "⚠️ The Gemini AI service is currently experiencing high demand.\n\n"
                    "Please wait a few moments and try again.\n\n"
                    f"Error Details: {e}"
                )