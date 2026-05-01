"""
State-specific election information selector component.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.data.state_data import get_states_list, get_state_info
from src.utils.i18n import t


def render_states(lang: str = "en") -> None:
    """Render the state information selector."""

    st.markdown(
        textwrap.dedent(f"""
            <h1 style="text-align:center; font-weight: 800; font-size: 2rem; margin-bottom: 1.5rem;">
                {t("state_title", lang)}
            </h1>
        """),
        unsafe_allow_html=True,
    )

    states = get_states_list()

    selected = st.selectbox(
        t("state_select", lang),
        options=states,
        index=None,
        key="state_selector",
        placeholder=t("state_select", lang),
    )

    if selected is None:
        # Show map-like prompt
        st.markdown(
            textwrap.dedent(f"""
                <div style="
                    text-align: center; padding: 3rem 2rem;
                    border-radius: 1.2rem;
                    background: rgba(255,255,255,0.03);
                    border: 1px dashed rgba(255,255,255,0.15);
                ">
                    <p style="font-size: 3rem; margin: 0;">🗺️</p>
                    <p style="opacity: 0.6; margin: 0.5rem 0 0 0;">
                        {'ऊपर ड्रॉपडाउन से एक राज्य/केंद्र शासित प्रदेश चुनें' if lang == 'hi'
                         else 'Select a state or UT from the dropdown above to see election details'}
                    </p>
                </div>
            """),
            unsafe_allow_html=True,
        )
        return

    info = get_state_info(selected, lang)

    # ── Info card ────────────────────────────────────────────────
    st.markdown(
        textwrap.dedent(f"""
            <div style="
                padding: 1.5rem 2rem;
                border-radius: 1.2rem;
                background: linear-gradient(145deg, rgba(255,107,53,0.06), rgba(255,107,53,0.02));
                border: 1px solid rgba(255,107,53,0.2);
                border-left: 5px solid #FF6B35;
                margin-bottom: 1rem;
            ">
                <h2 style="margin: 0 0 0.8rem 0; font-weight: 800; font-size: 1.4rem;">
                    🏛️ {selected}
                </h2>
            </div>
        """),
        unsafe_allow_html=True,
    )

    # Metrics grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Lok Sabha Seats" if lang == "en" else "लोकसभा सीटें",
            value=info.get("lok_sabha", "—"),
        )
    with col2:
        st.metric(
            label="Assembly Seats" if lang == "en" else "विधानसभा सीटें",
            value=info.get("assembly", "—"),
        )
    with col3:
        st.metric(
            label="Capital" if lang == "en" else "राजधानी",
            value=info.get("capital", "—"),
        )

    col4, col5 = st.columns(2)
    with col4:
        st.metric(
            label="Last Assembly Election" if lang == "en" else "पिछला विधानसभा चुनाव",
            value=info.get("last_assembly", "—"),
        )
    with col5:
        ceo_url = info.get("ceo_website", "eci.gov.in")
        st.markdown(
            f"""
            **{'CEO वेबसाइट' if lang == 'hi' else 'CEO Website'}:**
            [{ceo_url}](https://{ceo_url})
            """,
        )

    # Note
    if info.get("note"):
        st.info(f"📌 {info['note']}")
