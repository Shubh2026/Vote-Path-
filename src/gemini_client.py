"""
Google Gemini API client with rate-limiting and input sanitization.
"""

from __future__ import annotations

import google.generativeai as genai
from src.config import get_gemini_api_key, GEMINI_MODEL
from src.utils.sanitizer import sanitize_text
from src.utils.rate_limiter import RateLimiter

# Module-level rate limiter (shared across calls within a session)
_rate_limiter = RateLimiter(max_calls=10, window_seconds=60)

# Safety settings to ensure responsible AI usage
_SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

_SYSTEM_PROMPT = (
    "You are BharatVote Guide, an expert on Indian elections. "
    "Provide accurate, clear, and helpful information about the Indian election process, "
    "voter registration, ECI rules, and democratic participation. "
    "Keep answers concise (under 300 words). "
    "Be inclusive of all genders, ages, and backgrounds. "
    "If asked in Hindi, respond in Hindi. "
    "Never share false or misleading information about elections."
)


def _get_model() -> genai.GenerativeModel:
    """Initialise and return a Gemini model instance."""
    api_key = get_gemini_api_key()
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please configure it.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        safety_settings=_SAFETY_SETTINGS,
        system_instruction=_SYSTEM_PROMPT,
    )


def ask_gemini(user_query: str, language: str = "en") -> str:
    """
    Send a sanitised user query to Gemini and return the response text.

    Args:
        user_query: Raw user input (will be sanitised).
        language: 'en' for English, 'hi' for Hindi.

    Returns:
        Model response text, or an error/rate-limit message.
    """
    if not _rate_limiter.is_allowed():
        if language == "hi":
            return "⏳ कृपया कुछ समय बाद पुनः प्रयास करें। बहुत अधिक अनुरोध भेजे गए हैं।"
        return "⏳ Too many requests. Please wait a moment and try again."

    sanitised = sanitize_text(user_query)
    if not sanitised.strip():
        if language == "hi":
            return "❌ कृपया एक वैध प्रश्न दर्ज करें।"
        return "❌ Please enter a valid question."

    lang_instruction = (
        "Respond in Hindi (Devanagari script)." if language == "hi"
        else "Respond in English."
    )
    full_prompt = f"{lang_instruction}\n\nUser question: {sanitised}"

    try:
        _rate_limiter.record_call()
        model = _get_model()
        response = model.generate_content(full_prompt)
        
        if not response.candidates:
             return "⚠️ No response candidates were returned. This might be due to safety filters."
             
        # Check if the first candidate has parts (otherwise accessing .text will fail)
        if not response.candidates[0].content.parts:
            return "⚠️ The response was blocked by safety filters."

        return response.text
    except ValueError as ve:
        return f"⚠️ Configuration error: {ve}"
    except Exception as exc:  # noqa: BLE001
        return f"⚠️ Could not generate a response. Error: {exc}"
