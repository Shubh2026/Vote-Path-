"""
Simple in-memory rate limiter using a sliding-window approach.
"""

from __future__ import annotations

import time
from collections import deque


class RateLimiter:
    """
    Sliding-window rate limiter.

    Tracks call timestamps and rejects calls that exceed the limit
    within the configured time window.
    """

    def __init__(self, max_calls: int = 10, window_seconds: int = 60) -> None:
        self.max_calls = max_calls
        self.window_seconds = window_seconds
        self._timestamps: deque[float] = deque()

    def _purge_old(self) -> None:
        """Remove timestamps outside the current window."""
        cutoff = time.time() - self.window_seconds
        while self._timestamps and self._timestamps[0] < cutoff:
            self._timestamps.popleft()

    def is_allowed(self) -> bool:
        """Check whether a new call is within the rate limit."""
        self._purge_old()
        return len(self._timestamps) < self.max_calls

    def record_call(self) -> None:
        """Record a new call timestamp."""
        self._timestamps.append(time.time())

    def remaining(self) -> int:
        """Return how many calls are still allowed in this window."""
        self._purge_old()
        return max(0, self.max_calls - len(self._timestamps))
