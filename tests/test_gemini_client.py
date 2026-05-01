"""
Unit tests for the Gemini client (mocked — no real API calls).
"""

from unittest.mock import patch, MagicMock
import pytest

from src.gemini_client import ask_gemini


class TestAskGemini:
    """Tests for ask_gemini with mocked API."""

    @patch("src.gemini_client._rate_limiter")
    @patch("src.gemini_client._get_model")
    def test_successful_response(self, mock_model_fn, mock_limiter):
        mock_limiter.is_allowed.return_value = True
        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(text="Test response")
        mock_model_fn.return_value = mock_model

        result = ask_gemini("What is EVM?", language="en")
        assert result == "Test response"

    @patch("src.gemini_client._rate_limiter")
    def test_rate_limited_english(self, mock_limiter):
        mock_limiter.is_allowed.return_value = False
        result = ask_gemini("What is EVM?", language="en")
        assert "Too many requests" in result

    @patch("src.gemini_client._rate_limiter")
    def test_rate_limited_hindi(self, mock_limiter):
        mock_limiter.is_allowed.return_value = False
        result = ask_gemini("EVM क्या है?", language="hi")
        assert "कृपया" in result

    @patch("src.gemini_client._rate_limiter")
    def test_empty_query_english(self, mock_limiter):
        mock_limiter.is_allowed.return_value = True
        result = ask_gemini("", language="en")
        assert "valid question" in result.lower() or "❌" in result

    @patch("src.gemini_client._rate_limiter")
    def test_empty_query_hindi(self, mock_limiter):
        mock_limiter.is_allowed.return_value = True
        result = ask_gemini("   ", language="hi")
        assert "❌" in result

    @patch("src.gemini_client._rate_limiter")
    @patch("src.gemini_client._get_model")
    def test_api_error_handled(self, mock_model_fn, mock_limiter):
        mock_limiter.is_allowed.return_value = True
        mock_model = MagicMock()
        mock_model.generate_content.side_effect = Exception("API Error")
        mock_model_fn.return_value = mock_model

        result = ask_gemini("Test query")
        assert "⚠️" in result

    @patch("src.gemini_client._rate_limiter")
    @patch("src.gemini_client.get_gemini_api_key", return_value="")
    def test_missing_api_key(self, mock_key, mock_limiter):
        mock_limiter.is_allowed.return_value = True
        result = ask_gemini("Test query")
        assert "⚠️" in result or "error" in result.lower()

    @patch("src.gemini_client._rate_limiter")
    @patch("src.gemini_client._get_model")
    def test_html_stripped_from_input(self, mock_model_fn, mock_limiter):
        mock_limiter.is_allowed.return_value = True
        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(text="Safe response")
        mock_model_fn.return_value = mock_model

        result = ask_gemini("<script>alert('xss')</script>What is EVM?")
        assert result == "Safe response"
        # Verify the model received sanitized input
        call_args = mock_model.generate_content.call_args[0][0]
        assert "<script>" not in call_args
