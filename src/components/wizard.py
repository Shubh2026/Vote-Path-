"""
Step-by-step election wizard component.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.data.election_data import get_wizard_steps
from src.utils.i18n import t


_STEP_COLORS = [
    "#FF6B35", "#4CAF50", "#2196F3", "#F7C948", "#9C27B0", "#E91E63",
]


def render_wizard(lang: str = "en") -> None:
    """Render the step-by-step election guide wizard."""

    st.markdown(
        textwrap.dedent(f"""
            <h1 style="text-align:center; font-weight: 800; font-size: 2rem; margin-bottom: 1.5rem;">
                {t("wizard_title", lang)}
            </h1>
        """),
        unsafe_allow_html=True,
    )

    steps = get_wizard_steps(lang)
    total = len(steps)

    # Initialise wizard state
    if "wizard_step" not in st.session_state:
        st.session_state["wizard_step"] = 0

    current = st.session_state["wizard_step"]
    step = steps[current]
    color = _STEP_COLORS[current % len(_STEP_COLORS)]

    # ── Progress bar ─────────────────────────────────────────────
    progress_pct = (current + 1) / total
    st.progress(progress_pct)

    # Step indicator pills
    pill_html = '<div style="display:flex; justify-content:center; gap:0.4rem; margin-bottom:1.5rem; flex-wrap:wrap;">'
    for i, s in enumerate(steps):
        bg = _STEP_COLORS[i % len(_STEP_COLORS)] if i <= current else "rgba(255,255,255,0.1)"
        text_color = "#fff" if i <= current else "rgba(255,255,255,0.4)"
        pill_html += textwrap.dedent(f"""
            <div role="tab" aria-selected="{'true' if i == current else 'false'}"
                 aria-label="{t('wizard_step', lang)} {i+1}"
                 style="
                    padding: 0.3rem 0.8rem; border-radius: 999px;
                    font-size: 0.75rem; font-weight: 600;
                    background: {bg}; color: {text_color};
                    transition: all 0.2s ease;
                 ">
                {s['icon']} {i + 1}
            </div>
        """)
    pill_html += "</div>"
    st.markdown(pill_html, unsafe_allow_html=True)

    # ── Step content card ────────────────────────────────────────
    st.markdown(
        textwrap.dedent(f"""
            <div role="tabpanel" aria-label="{step['title']}" style="
                padding: 2rem;
                border-radius: 1.2rem;
                background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
                border: 1px solid {color}33;
                border-top: 4px solid {color};
                margin-bottom: 1.5rem;
            ">
                <div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 1rem;">
                    <span style="font-size: 2rem;">{step['icon']}</span>
                    <div>
                        <span style="
                            font-size: 0.7rem; font-weight: 700; padding: 0.15rem 0.6rem;
                            border-radius: 999px; background: {color}22; color: {color};
                            text-transform: uppercase;
                        ">{t('wizard_step', lang)} {step['step']}/{total}</span>
                        <h2 style="margin: 0.3rem 0 0 0; font-size: 1.4rem; font-weight: 800; color: white;">
                            {step['title']}
                        </h2>
                    </div>
                </div>
            </div>
        """),
        unsafe_allow_html=True,
    )

    # Render the markdown content inside Streamlit for proper formatting
    st.markdown(step["content"])

    # ── Navigation buttons ───────────────────────────────────────
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if current > 0:
            if st.button(
                t("wizard_prev", lang),
                key="wizard_prev_btn",
                use_container_width=True,
            ):
                st.session_state["wizard_step"] = current - 1
                st.rerun()

    with col3:
        if current < total - 1:
            if st.button(
                t("wizard_next", lang),
                key="wizard_next_btn",
                use_container_width=True,
                type="primary",
            ):
                st.session_state["wizard_step"] = current + 1
                st.rerun()
