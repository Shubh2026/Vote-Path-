"""
BharatVote Guide — main Streamlit application entry point.

An interactive, accessible, bilingual web app that educates Indian citizens
about the complete election process.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.config import APP_TITLE, APP_ICON
from src.components import (
    render_home,
    render_timeline,
    render_wizard,
    render_quiz,
    render_faq,
    render_states,
    render_ai_chat,
    render_sidebar,
)

# ═══════════════════════════════════════════════════════════════════
# Page configuration — MUST be the first Streamlit command
# ═══════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "BharatVote Guide — Educating India about its elections. "
                 "Powered by Google Gemini.",
    },
)


# ═══════════════════════════════════════════════════════════════════
# Custom CSS — premium look, accessibility, responsive
# ═══════════════════════════════════════════════════════════════════
st.html(
    textwrap.dedent("""
        <style>
        /* ── Import Google Fonts ────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        /* ── Global ─────────────────────────────────────────────── */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* Remove default Streamlit header padding */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        /* ── Sidebar styling ────────────────────────────────────── */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0E1117 0%, #141824 100%);
        }

        [data-testid="stSidebar"] [data-testid="stButton"] button {
            border-radius: 0.7rem;
            font-weight: 600;
            font-size: 0.85rem;
            text-align: left;
            padding: 0.55rem 1rem;
            transition: all 0.2s ease;
        }

        /* ── Button styling ─────────────────────────────────────── */
        .stButton > button {
            border-radius: 0.7rem;
            font-weight: 600;
            transition: all 0.15s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(255, 107, 53, 0.25);
        }

        .stButton > button:focus-visible {
            outline: 3px solid #F7C948;
            outline-offset: 2px;
        }

        /* ── Expander styling ───────────────────────────────────── */
        .streamlit-expanderHeader {
            font-weight: 600;
            font-size: 0.95rem;
            border-radius: 0.7rem;
        }

        /* ── Metric cards ───────────────────────────────────────── */
        [data-testid="stMetric"] {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 1rem;
            padding: 1rem;
        }

        [data-testid="stMetricValue"] {
            font-weight: 800;
            color: #FF6B35;
        }

        /* ── Progress bar ───────────────────────────────────────── */
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #FF6B35, #F7C948);
            border-radius: 999px;
        }

        /* ── Chat messages ──────────────────────────────────────── */
        [data-testid="stChatMessage"] {
            border-radius: 1rem;
            border: 1px solid rgba(255,255,255,0.06);
        }

        /* ── Focus / accessibility ──────────────────────────────── */
        *:focus-visible {
            outline: 2px solid #F7C948;
            outline-offset: 2px;
        }

        /* ── Selectbox ───────────────────────────────────────────── */
        [data-testid="stSelectbox"] div[data-baseweb="select"] {
            border-radius: 0.7rem;
        }

        /* ── Radio buttons ──────────────────────────────────────── */
        .stRadio > div {
            gap: 0.3rem;
        }

        .stRadio > div > label {
            padding: 0.6rem 1rem;
            border-radius: 0.7rem;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.15s ease;
            cursor: pointer;
        }

        .stRadio > div > label:hover {
            border-color: #FF6B35;
            background: rgba(255,107,53,0.08);
        }

        /* ── Responsive ─────────────────────────────────────────── */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }

        /* ── Skip-to-content link (accessibility) ───────────────── */
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: #FF6B35;
            color: #fff;
            padding: 8px 16px;
            z-index: 100;
            border-radius: 0 0 8px 0;
            font-weight: 700;
            text-decoration: none;
        }
        .skip-link:focus {
            top: 0;
        }

        /* ── Smooth scrolling ───────────────────────────────────── */
        html {
            scroll-behavior: smooth;
        }
        </style>

        <!-- Accessibility: skip-to-content link -->
        <a href="#main-content" class="skip-link" tabindex="0">Skip to main content</a>
    """).strip()
)


# ═══════════════════════════════════════════════════════════════════
# Initialise session state
# ═══════════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"
if "page" not in st.session_state:
    st.session_state["page"] = "home"


# ═══════════════════════════════════════════════════════════════════
# Render sidebar + get active page
# ═══════════════════════════════════════════════════════════════════
current_page = render_sidebar()
lang = st.session_state["lang"]


# ═══════════════════════════════════════════════════════════════════
# Main content area
# ═══════════════════════════════════════════════════════════════════
st.markdown('<div id="main-content" role="main">', unsafe_allow_html=True)

_PAGE_RENDERERS = {
    "home": render_home,
    "timeline": render_timeline,
    "wizard": render_wizard,
    "quiz": render_quiz,
    "faq": render_faq,
    "states": render_states,
    "ask_ai": render_ai_chat,
}

renderer = _PAGE_RENDERERS.get(current_page, render_home)
renderer(lang=lang)

st.markdown("</div>", unsafe_allow_html=True)
