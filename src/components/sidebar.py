"""
Sidebar component — navigation, language toggle, theme info.
"""

from __future__ import annotations

import textwrap
import streamlit as st
from src.utils.i18n import t


def render_sidebar() -> str:
    """
    Render the sidebar and return the selected page key.

    Returns:
        The navigation key for the selected page.
    """
    with st.sidebar:
        # ── Brand Logo ───────────────────────────────────────────
        st.html(
            textwrap.dedent(f"""
                <div style="display: flex; align-items: center; gap: 0.8rem; padding: 0.5rem 0; margin-bottom: 1.5rem;">
                    <div style="
                        background: linear-gradient(135deg, #FF6B35 0%, #F7C948 100%);
                        width: 42px; height: 42px; border-radius: 12px;
                        display: flex; align-items: center; justify-content: center;
                        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.4);
                    ">
                        <span style="font-size: 1.6rem;">🗳️</span>
                    </div>
                    <div>
                        <div style="font-weight: 900; font-size: 1.2rem; line-height: 1; color: white; letter-spacing: -0.5px;">
                            BharatVote
                        </div>
                        <div style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; color: #F7C948; margin-top: 3px;">
                            Guide • भारतवोट
                        </div>
                    </div>
                </div>
            """).strip()
        )

        # ── Language toggle ──────────────────────────────────────
        st.markdown("### " + t("sidebar_language", st.session_state.get("lang", "en")))
        lang_options = {"English 🇮🇳": "en", "हिन्दी 🇮🇳": "hi"}
        current_lang = st.session_state.get("lang", "en")
        default_idx = 0 if current_lang == "en" else 1
        selected_label = st.radio(
            label="Language",
            options=list(lang_options.keys()),
            index=default_idx,
            label_visibility="collapsed",
            key="lang_radio",
        )
        st.session_state["lang"] = lang_options[selected_label]
        lang = st.session_state["lang"]

        st.divider()

        # ── Navigation ───────────────────────────────────────────
        nav_items = [
            ("home", t("nav_home", lang)),
            ("timeline", t("nav_timeline", lang)),
            ("wizard", t("nav_wizard", lang)),
            ("quiz", t("nav_quiz", lang)),
            ("faq", t("nav_faq", lang)),
            ("states", t("nav_states", lang)),
            ("ask_ai", t("nav_ask_ai", lang)),
        ]

        current_page = st.session_state.get("page", "home")
        for key, label in nav_items:
            button_type = "primary" if current_page == key else "secondary"
            if st.button(label, key=f"nav_{key}", use_container_width=True, type=button_type):
                st.session_state["page"] = key
                st.rerun()

        st.divider()

        # ── Footer ───────────────────────────────────────────────
        st.caption(t("footer_text", lang))
        st.caption("v1.0.0 • © 2025")

    return st.session_state.get("page", "home")
