"""
AI Chat component — powered by Google Gemini.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.gemini_client import ask_gemini
from src.utils.i18n import t


def render_ai_chat(lang: str = "en") -> None:
    """Render the AI assistant chat interface."""

    st.markdown(
        textwrap.dedent(f"""
            <h1 style="text-align:center; font-weight: 800; font-size: 2rem; margin-bottom: 0.3rem;">
                {t("ai_title", lang)}
            </h1>
            <p style="text-align:center; opacity: 0.6; margin-bottom: 1.5rem; font-size: 0.85rem;">
                {t("ai_disclaimer", lang)}
            </p>
        """),
        unsafe_allow_html=True,
    )

    # ── Chat history ─────────────────────────────────────────────
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Display previous messages
    for msg in st.session_state["chat_history"]:
        role = msg["role"]
        with st.chat_message(role, avatar="🙋" if role == "user" else "🤖"):
            st.markdown(msg["content"])

    # ── Suggested questions ──────────────────────────────────────
    if not st.session_state["chat_history"]:
        suggestions = (
            [
                "मतदाता आईडी कैसे बनवाएँ?",
                "EVM क्या है?",
                "NOTA कब शुरू हुआ?",
                "चुनाव में कितना खर्च कर सकते हैं?",
            ]
            if lang == "hi"
            else [
                "How do I register as a voter?",
                "What is an EVM?",
                "How does vote counting work?",
                "What is the Model Code of Conduct?",
            ]
        )

        st.markdown(
            textwrap.dedent(f"""
                <div style="
                    padding: 1.5rem;
                    border-radius: 1rem;
                    background: rgba(156,39,176,0.06);
                    border: 1px solid rgba(156,39,176,0.15);
                    margin-bottom: 1rem;
                ">
                    <p style="font-weight: 600; margin: 0 0 0.5rem 0;">
                        {'💡 सुझाए गए प्रश्न:' if lang == 'hi' else '💡 Suggested questions:'}
                    </p>
                </div>
            """),
            unsafe_allow_html=True,
        )

        cols = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(
                    suggestion,
                    key=f"suggestion_{i}",
                    use_container_width=True,
                ):
                    _handle_query(suggestion, lang)
                    st.rerun()

    # ── Input ────────────────────────────────────────────────────
    user_input = st.chat_input(
        placeholder=t("ai_placeholder", lang),
    )

    if user_input:
        _handle_query(user_input, lang)
        st.rerun()


def _handle_query(query: str, lang: str) -> None:
    """Send query to Gemini and store in chat history."""
    st.session_state["chat_history"].append(
        {"role": "user", "content": query}
    )

    response = ask_gemini(query, language=lang)

    st.session_state["chat_history"].append(
        {"role": "assistant", "content": response}
    )
