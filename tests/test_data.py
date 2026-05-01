"""
Unit tests for election data modules.
"""

import pytest

from src.data.election_data import get_timeline_data, get_wizard_steps
from src.data.quiz_data import get_quiz_questions
from src.data.faq_data import get_faqs
from src.data.state_data import get_states_list, get_state_info


class TestTimelineData:
    """Tests for election timeline data."""

    def test_english_has_six_phases(self):
        data = get_timeline_data("en")
        assert len(data) == 6

    def test_hindi_has_six_phases(self):
        data = get_timeline_data("hi")
        assert len(data) == 6

    def test_phase_structure(self):
        for phase in get_timeline_data("en"):
            assert "phase" in phase
            assert "title" in phase
            assert "icon" in phase
            assert "date" in phase
            assert "desc" in phase
            assert "details" in phase


class TestWizardSteps:
    """Tests for wizard step data."""

    def test_english_has_six_steps(self):
        steps = get_wizard_steps("en")
        assert len(steps) == 6

    def test_hindi_has_six_steps(self):
        steps = get_wizard_steps("hi")
        assert len(steps) == 6

    def test_step_structure(self):
        for step in get_wizard_steps("en"):
            assert "step" in step
            assert "title" in step
            assert "icon" in step
            assert "content" in step

    def test_steps_are_sequential(self):
        steps = get_wizard_steps("en")
        for i, step in enumerate(steps):
            assert step["step"] == i + 1


class TestQuizData:
    """Tests for quiz questions."""

    def test_english_has_ten_questions(self):
        questions = get_quiz_questions("en")
        assert len(questions) == 10

    def test_hindi_has_ten_questions(self):
        questions = get_quiz_questions("hi")
        assert len(questions) == 10

    def test_question_structure(self):
        for q in get_quiz_questions("en"):
            assert "q" in q
            assert "options" in q
            assert "answer" in q
            assert "explanation" in q
            assert len(q["options"]) == 4
            assert 0 <= q["answer"] <= 3

    def test_answer_index_valid(self):
        for q in get_quiz_questions("en"):
            assert q["answer"] < len(q["options"])


class TestFaqData:
    """Tests for FAQ data."""

    def test_english_has_faqs(self):
        faqs = get_faqs("en")
        assert len(faqs) >= 5

    def test_hindi_has_faqs(self):
        faqs = get_faqs("hi")
        assert len(faqs) >= 5

    def test_faq_structure(self):
        for faq in get_faqs("en"):
            assert "q" in faq
            assert "a" in faq
            assert len(faq["q"]) > 0
            assert len(faq["a"]) > 0


class TestStateData:
    """Tests for state information."""

    def test_states_list_not_empty(self):
        states = get_states_list()
        assert len(states) >= 36  # 28 states + 8 UTs

    def test_punjab_in_list(self):
        states = get_states_list()
        assert "Punjab" in states

    def test_state_info_punjab(self):
        info = get_state_info("Punjab", "en")
        assert info["lok_sabha"] == 13
        assert info["assembly"] == 117
        assert info["capital"] == "Chandigarh"

    def test_state_info_hindi(self):
        info = get_state_info("Punjab", "hi")
        assert info["lok_sabha"] == 13
        assert "चंडीगढ़" in info["capital"]

    def test_unknown_state_returns_fallback(self):
        info = get_state_info("UnknownState", "en")
        assert info["lok_sabha"] == "—"
        assert "eci.gov.in" in info["ceo_website"]

    def test_uttar_pradesh_has_80_seats(self):
        info = get_state_info("Uttar Pradesh", "en")
        assert info["lok_sabha"] == 80
