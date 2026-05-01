"""
Unit tests for the input sanitizer.
"""

import pytest
from src.utils.sanitizer import sanitize_text, MAX_INPUT_LENGTH


class TestSanitizeText:
    """Tests for sanitize_text function."""

    def test_normal_input(self):
        assert sanitize_text("How do I register to vote?") == "How do I register to vote?"

    def test_strips_html_tags(self):
        result = sanitize_text("<script>alert('xss')</script>Hello")
        assert "<script>" not in result
        assert "</script>" not in result
        assert "Hello" in result

    def test_strips_all_html(self):
        result = sanitize_text("<b>Bold</b> <i>Italic</i> <a href='x'>Link</a>")
        assert "<b>" not in result
        assert "<i>" not in result
        assert "<a" not in result
        assert "Bold" in result

    def test_truncates_long_input(self):
        long_input = "A" * (MAX_INPUT_LENGTH + 500)
        result = sanitize_text(long_input)
        assert len(result) <= MAX_INPUT_LENGTH

    def test_empty_string(self):
        assert sanitize_text("") == ""

    def test_whitespace_only(self):
        assert sanitize_text("   ") == ""

    def test_non_string_input(self):
        assert sanitize_text(123) == ""  # type: ignore[arg-type]
        assert sanitize_text(None) == ""  # type: ignore[arg-type]

    def test_collapses_whitespace(self):
        result = sanitize_text("Hello     World")
        assert result == "Hello World"

    def test_preserves_newlines(self):
        result = sanitize_text("Line one\nLine two")
        assert "\n" in result

    def test_collapses_excessive_newlines(self):
        result = sanitize_text("A\n\n\n\n\nB")
        assert result == "A\n\nB"

    def test_hindi_text(self):
        hindi = "मतदाता पहचान पत्र कैसे बनवाएँ?"
        assert sanitize_text(hindi) == hindi

    def test_mixed_language(self):
        mixed = "How to register? मतदाता पंजीकरण"
        assert sanitize_text(mixed) == mixed
