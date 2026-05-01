"""
FAQ component with expandable question–answer pairs.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.data.faq_data import get_faqs
from src.utils.i18n import t


def render_faq(lang: str = "en") -> None:
    """Render the FAQ section."""

    st.markdown(
        textwrap.dedent(f"""
            <h1 style="text-align:center; font-weight: 800; font-size: 2rem; margin-bottom: 0.5rem;">
                {t("faq_title", lang)}
            </h1>
            <p style="text-align:center; opacity: 0.6; margin-bottom: 2rem;">
                {'सबसे अधिक पूछे जाने वाले प्रश्नों के उत्तर' if lang == 'hi'
                 else 'Quick answers to the most common questions about Indian elections'}
            </p>
        """),
        unsafe_allow_html=True,
    )

    faqs = get_faqs(lang)

    for idx, faq in enumerate(faqs):
        with st.expander(f"**{faq['q']}**", expanded=False):
            st.markdown(faq["a"])
            # Link to AI for deeper questions
            deeper = (
                "🤖 और जानना चाहते हैं? AI से पूछें!"
                if lang == "hi"
                else "🤖 Want to know more? Ask the AI Assistant!"
            )
            st.caption(deeper)
