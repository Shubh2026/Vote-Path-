"""
Unit tests for the i18n translation system.
"""

import pytest
from src.utils.i18n import t


class TestTranslation:
    """Tests for the t() translation function."""

    def test_english_translation(self):
        result = t("app_title", "en")
        assert "BharatVote" in result

    def test_hindi_translation(self):
        result = t("app_title", "hi")
        assert "भारतवोट" in result

    def test_unknown_key_returns_key(self):
        assert t("nonexistent_key_xyz", "en") == "nonexistent_key_xyz"

    def test_fallback_to_english(self):
        # Even with unsupported lang, should fall back to English
        result = t("app_title", "fr")
        assert "BharatVote" in result

    def test_all_nav_keys_exist(self):
        nav_keys = [
            "nav_home", "nav_timeline", "nav_wizard",
            "nav_quiz", "nav_faq", "nav_states", "nav_ask_ai",
        ]
        for key in nav_keys:
            en = t(key, "en")
            hi = t(key, "hi")
            assert en != key, f"Missing English for {key}"
            assert hi != key, f"Missing Hindi for {key}"

    def test_quiz_keys_exist(self):
        quiz_keys = [
            "quiz_title", "quiz_start", "quiz_submit",
            "quiz_next", "quiz_score", "quiz_correct",
            "quiz_wrong", "quiz_restart",
        ]
        for key in quiz_keys:
            assert t(key, "en") != key
            assert t(key, "hi") != key
