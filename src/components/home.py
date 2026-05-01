"""
Home page component — hero section with feature cards.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.utils.i18n import t


def render_home(lang: str = "en") -> None:
    """Render the home / landing page."""

    # ── Hero section ─────────────────────────────────────────────
    st.html(
        textwrap.dedent(f"""
            <div role="banner" style="
                text-align: center;
                padding: 3rem 1rem 2rem 1rem;
                border-radius: 1.5rem;
                background: linear-gradient(135deg, #1a1140 0%, #2d1b69 30%, #0f3460 70%, #0a1628 100%);
                margin-bottom: 2rem;
                position: relative;
                overflow: hidden;
            ">
                <div style="
                    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
                    background: radial-gradient(circle at 20% 50%, rgba(255,107,53,0.15) 0%, transparent 50%),
                                 radial-gradient(circle at 80% 20%, rgba(247,201,72,0.1) 0%, transparent 40%);
                    pointer-events: none;
                "></div>
                <div style="position: relative; z-index: 1;">
                    <p style="font-size: 4rem; margin: 0; line-height: 1;">🗳️</p>
                    <h1 style="
                        font-size: 2.6rem; font-weight: 900; margin: 0.5rem 0;
                        background: linear-gradient(135deg, #FF6B35, #F7C948, #FF6B35);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        letter-spacing: -0.5px;
                    " aria-label="{t('home_hero_title', lang)}">
                        {t("home_hero_title", lang)}
                    </h1>
                    <p style="
                        font-size: 1.15rem; opacity: 0.85; max-width: 600px;
                        margin: 0.5rem auto 0; color: #e0e0e0; line-height: 1.6;
                    ">
                        {t("home_hero_subtitle", lang)}
                    </p>
                </div>
            </div>
        """).strip()
    )

    # ── Feature cards ────────────────────────────────────────────
    cards = [
        {
            "icon": "📅",
            "title": t("home_card_timeline", lang),
            "desc": t("home_card_timeline_desc", lang),
            "color": "#FF6B35",
            "page": "timeline",
        },
        {
            "icon": "🧭",
            "title": t("home_card_wizard", lang),
            "desc": t("home_card_wizard_desc", lang),
            "color": "#4CAF50",
            "page": "wizard",
        },
        {
            "icon": "📝",
            "title": t("home_card_quiz", lang),
            "desc": t("home_card_quiz_desc", lang),
            "color": "#2196F3",
            "page": "quiz",
        },
        {
            "icon": "🤖",
            "title": t("home_card_ai", lang),
            "desc": t("home_card_ai_desc", lang),
            "color": "#9C27B0",
            "page": "ask_ai",
        },
    ]

    cols = st.columns(2)
    for idx, card in enumerate(cards):
        with cols[idx % 2]:
            st.html(
                textwrap.dedent(f"""
                    <div role="article" aria-label="{card['title']}" style="
                        padding: 1.5rem;
                        border-radius: 1rem;
                        background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
                        border: 1px solid rgba(255,255,255,0.08);
                        margin-bottom: 1rem;
                        backdrop-filter: blur(10px);
                        transition: transform 0.2s ease, box-shadow 0.2s ease;
                        min-height: 180px;
                    ">
                        <div style="
                            width: 48px; height: 48px; border-radius: 12px;
                            background: {card['color']}22;
                            display: flex; align-items: center; justify-content: center;
                            font-size: 1.5rem; margin-bottom: 0.8rem;
                        ">{card['icon']}</div>
                        <h3 style="
                            margin: 0 0 0.4rem 0; font-size: 1.1rem; font-weight: 700;
                            color: {card['color']};
                        ">{card['title']}</h3>
                        <p style="
                            margin: 0; font-size: 0.88rem; opacity: 0.75; line-height: 1.5;
                            color: #ddd;
                        ">{card['desc']}</p>
                    </div>
                """).strip()
            )
            if st.button(
                f"→ {card['title']}",
                key=f"home_card_{card['page']}",
                use_container_width=True,
            ):
                st.session_state["page"] = card["page"]
                st.rerun()

    # ── Quick stats ──────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)

    stats = [
        ("96.88 Cr", "Registered Voters (2024)" if lang == "en" else "पंजीकृत मतदाता (2024)"),
        ("543", "Lok Sabha Seats" if lang == "en" else "लोकसभा सीटें"),
        ("28 + 8", "States & UTs" if lang == "en" else "राज्य और केंद्र शासित प्रदेश"),
        ("1951", "First Election" if lang == "en" else "पहला चुनाव"),
    ]

    stat_cols = st.columns(4)
    for i, (value, label) in enumerate(stats):
        with stat_cols[i]:
            st.html(
                textwrap.dedent(f"""
                    <div style="
                        text-align: center; padding: 1.2rem 0.5rem;
                        border-radius: 1rem;
                        background: rgba(255,255,255,0.03);
                        border: 1px solid rgba(255,255,255,0.06);
                    ">
                        <p style="
                            font-size: 1.5rem; font-weight: 800; margin: 0;
                            background: linear-gradient(135deg, #FF6B35, #F7C948);
                            -webkit-background-clip: text;
                            -webkit-text-fill-color: transparent;
                        ">{value}</p>
                        <p style="font-size: 0.72rem; opacity: 0.6; margin: 0.2rem 0 0 0; color: #aaa;">
                            {label}
                        </p>
                    </div>
                """).strip()
            )
