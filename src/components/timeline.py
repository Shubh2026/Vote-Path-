"""
Interactive election timeline component.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.data.election_data import get_timeline_data
from src.utils.i18n import t


_PHASE_COLORS = [
    "#FF6B35", "#F7C948", "#4CAF50", "#2196F3", "#9C27B0", "#E91E63",
]


def render_timeline(lang: str = "en") -> None:
    """Render the interactive election timeline."""

    st.html(
        textwrap.dedent(f"""
            <div style="text-align:center; margin-bottom: 2rem;">
                <h1 style="font-weight: 800; font-size: 2rem;">
                    {t("timeline_title", lang)}
                </h1>
                <p style="opacity: 0.7; max-width: 600px; margin: 0 auto;">
                    {t("timeline_subtitle", lang)}
                </p>
            </div>
        """).strip()
    )

    timeline_data = get_timeline_data(lang)

    for idx, phase in enumerate(timeline_data):
        color = _PHASE_COLORS[idx % len(_PHASE_COLORS)]
        
        # Prepare the line connecting nodes
        line_html = ""
        if idx < len(timeline_data) - 1:
            line_html = f'<div style="width: 3px; height: 60px; background: linear-gradient(180deg, {color}44, transparent); margin-top: 4px;"></div>'

        # Main timeline entry
        html_content = textwrap.dedent(f"""
            <div role="listitem" aria-label="{phase['title']}" style="
                display: flex; align-items: flex-start; gap: 1.2rem;
                margin-bottom: 0.5rem; position: relative;
            ">
                <div style="display: flex; flex-direction: column; align-items: center; min-width: 50px;">
                    <div style="
                        width: 44px; height: 44px; border-radius: 50%;
                        background: {color}22; border: 3px solid {color};
                        display: flex; align-items: center; justify-content: center;
                        font-size: 1.3rem; flex-shrink: 0;
                    ">{phase['icon']}</div>
                    {line_html}
                </div>

                <div style="
                    flex: 1; padding: 1.2rem 1.5rem;
                    border-radius: 1rem;
                    background: rgba(255, 255, 255, 0.03);
                    border: 1px solid {color}33;
                    border-left: 4px solid {color};
                ">
                    <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
                        <span style="
                            font-size: 0.7rem; font-weight: 700; padding: 0.15rem 0.6rem;
                            border-radius: 999px; background: {color}22; color: {color};
                            text-transform: uppercase; letter-spacing: 0.5px;
                        ">Phase {phase['phase']}</span>
                        <span style="font-size: 0.75rem; opacity: 0.5;">{phase['date']}</span>
                    </div>
                    <h3 style="margin: 0.5rem 0 0.3rem 0; font-size: 1.15rem; font-weight: 700; color: white;">
                        {phase['title']}
                    </h3>
                    <p style="margin: 0; font-size: 0.9rem; opacity: 0.8; line-height: 1.6; color: #ddd;">
                        {phase['desc']}
                    </p>
                </div>
            </div>
        """).strip()
        
        st.html(html_content)

        # Expandable details
        detail_label = "📖 Details" if lang == "en" else "📖 विवरण"
        with st.expander(detail_label, expanded=False):
            st.markdown(phase["details"])
