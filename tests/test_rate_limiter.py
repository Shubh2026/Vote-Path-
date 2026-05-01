"""
Unit tests for the rate limiter.
"""

import time
from unittest.mock import patch

import pytest
from src.utils.rate_limiter import RateLimiter


class TestRateLimiter:
    """Tests for RateLimiter class."""

    def test_allows_within_limit(self):
        rl = RateLimiter(max_calls=5, window_seconds=60)
        for _ in range(5):
            assert rl.is_allowed()
            rl.record_call()

    def test_blocks_over_limit(self):
        rl = RateLimiter(max_calls=3, window_seconds=60)
        for _ in range(3):
            rl.record_call()
        assert not rl.is_allowed()

    def test_remaining_count(self):
        rl = RateLimiter(max_calls=5, window_seconds=60)
        assert rl.remaining() == 5
        rl.record_call()
        assert rl.remaining() == 4
        rl.record_call()
        rl.record_call()
        assert rl.remaining() == 2

    def test_window_expiry(self):
        rl = RateLimiter(max_calls=2, window_seconds=1)
        rl.record_call()
        rl.record_call()
        assert not rl.is_allowed()
        time.sleep(1.1)
        assert rl.is_allowed()

    def test_remaining_never_negative(self):
        rl = RateLimiter(max_calls=1, window_seconds=60)
        rl.record_call()
        rl.record_call()  # over-record
        assert rl.remaining() == 0

    def test_default_values(self):
        rl = RateLimiter()
        assert rl.max_calls == 10
        assert rl.window_seconds == 60
