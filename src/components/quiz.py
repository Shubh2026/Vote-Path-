"""
Interactive election quiz component with score tracking.
"""

from __future__ import annotations

import textwrap
import streamlit as st

from src.data.quiz_data import get_quiz_questions
from src.utils.i18n import t


def render_quiz(lang: str = "en") -> None:
    """Render the interactive election knowledge quiz."""

    st.markdown(
        textwrap.dedent(f"""
            <h1 style="text-align:center; font-weight: 800; font-size: 2rem; margin-bottom: 1.5rem;">
                {t("quiz_title", lang)}
            </h1>
        """),
        unsafe_allow_html=True,
    )

    questions = get_quiz_questions(lang)
    total = len(questions)

    # ── Initialise quiz state ────────────────────────────────────
    if "quiz_started" not in st.session_state:
        st.session_state["quiz_started"] = False
    if "quiz_idx" not in st.session_state:
        st.session_state["quiz_idx"] = 0
    if "quiz_score" not in st.session_state:
        st.session_state["quiz_score"] = 0
    if "quiz_answered" not in st.session_state:
        st.session_state["quiz_answered"] = False
    if "quiz_finished" not in st.session_state:
        st.session_state["quiz_finished"] = False

    # ── Start screen ─────────────────────────────────────────────
    if not st.session_state["quiz_started"]:
        st.markdown(
            textwrap.dedent(f"""
                <div style="
                    text-align: center; padding: 3rem 2rem;
                    border-radius: 1.2rem;
                    background: linear-gradient(145deg, rgba(33,150,243,0.08), rgba(33,150,243,0.02));
                    border: 1px solid rgba(33,150,243,0.2);
                ">
                    <p style="font-size: 3rem; margin: 0;">🧠</p>
                    <h2 style="margin: 0.5rem 0; font-weight: 700;">
                        {'क्या आप तैयार हैं?' if lang == 'hi' else 'Are you ready?'}
                    </h2>
                    <p style="opacity: 0.7; margin-bottom: 1.5rem;">
                        {total} {'प्रश्न • बहुविकल्पीय' if lang == 'hi' else 'questions • Multiple choice'}
                    </p>
                </div>
            """),
            unsafe_allow_html=True,
        )
        if st.button(
            t("quiz_start", lang),
            key="quiz_start_btn",
            use_container_width=True,
            type="primary",
        ):
            st.session_state["quiz_started"] = True
            st.session_state["quiz_idx"] = 0
            st.session_state["quiz_score"] = 0
            st.session_state["quiz_answered"] = False
            st.session_state["quiz_finished"] = False
            st.rerun()
        return

    # ── Results screen ───────────────────────────────────────────
    if st.session_state["quiz_finished"]:
        score = st.session_state["quiz_score"]
        pct = int((score / total) * 100)

        if pct >= 80:
            emoji, msg = "🏆", "Excellent!" if lang == "en" else "उत्कृष्ट!"
            color = "#4CAF50"
        elif pct >= 50:
            emoji, msg = "👍", "Good job!" if lang == "en" else "अच्छा!"
            color = "#F7C948"
        else:
            emoji, msg = "📚", "Keep learning!" if lang == "en" else "सीखते रहें!"
            color = "#FF6B35"

        st.markdown(
            textwrap.dedent(f"""
                <div style="
                    text-align: center; padding: 3rem 2rem;
                    border-radius: 1.2rem;
                    background: linear-gradient(145deg, {color}11, {color}05);
                    border: 1px solid {color}33;
                ">
                    <p style="font-size: 3.5rem; margin: 0;">{emoji}</p>
                    <h2 style="margin: 0.5rem 0; font-weight: 800; color: {color};">
                        {msg}
                    </h2>
                    <p style="font-size: 2rem; font-weight: 800; margin: 0.5rem 0;">
                        {t("quiz_score", lang)}: {score}/{total}
                    </p>
                    <p style="font-size: 1rem; opacity: 0.6;">({pct}%)</p>
                </div>
            """),
            unsafe_allow_html=True,
        )

        if st.button(
            t("quiz_restart", lang),
            key="quiz_restart_btn",
            use_container_width=True,
            type="primary",
        ):
            st.session_state["quiz_started"] = False
            st.session_state["quiz_idx"] = 0
            st.session_state["quiz_score"] = 0
            st.session_state["quiz_answered"] = False
            st.session_state["quiz_finished"] = False
            st.rerun()
        return

    # ── Question screen ──────────────────────────────────────────
    idx = st.session_state["quiz_idx"]
    q = questions[idx]

    # Progress
    st.progress((idx + 1) / total)
    st.markdown(
        f"**{t('quiz_question', lang)} {idx + 1}/{total}**",
    )

    # Question card
    st.markdown(
        textwrap.dedent(f"""
            <div style="
                padding: 1.5rem;
                border-radius: 1rem;
                background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
                border: 1px solid rgba(255,255,255,0.1);
                margin-bottom: 1rem;
            ">
                <h3 style="margin: 0; font-size: 1.15rem; font-weight: 700; line-height: 1.5;">
                    {q['q']}
                </h3>
            </div>
        """),
        unsafe_allow_html=True,
    )

    # Options
    selected = st.radio(
        "Options",
        options=q["options"],
        index=None,
        key=f"quiz_opt_{idx}",
        label_visibility="collapsed",
    )

    if not st.session_state["quiz_answered"]:
        if st.button(
            t("quiz_submit", lang),
            key="quiz_submit_btn",
            use_container_width=True,
            type="primary",
            disabled=selected is None,
        ):
            st.session_state["quiz_answered"] = True
            if selected == q["options"][q["answer"]]:
                st.session_state["quiz_score"] += 1
            st.rerun()
    else:
        # Show result
        correct_answer = q["options"][q["answer"]]
        if selected == correct_answer:
            st.success(t("quiz_correct", lang))
        else:
            st.error(
                f"{t('quiz_wrong', lang)} — "
                f"{'सही उत्तर' if lang == 'hi' else 'Correct answer'}: **{correct_answer}**"
            )

        # Explanation
        st.info(f"💡 {q['explanation']}")

        # Next / Finish
        if idx < total - 1:
            if st.button(
                t("quiz_next", lang),
                key="quiz_next_btn",
                use_container_width=True,
                type="primary",
            ):
                st.session_state["quiz_idx"] = idx + 1
                st.session_state["quiz_answered"] = False
                st.rerun()
        else:
            finish_label = "🏁 Finish" if lang == "en" else "🏁 समाप्त"
            if st.button(
                finish_label,
                key="quiz_finish_btn",
                use_container_width=True,
                type="primary",
            ):
                st.session_state["quiz_finished"] = True
                st.rerun()
