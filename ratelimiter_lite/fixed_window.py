import time
import threading

from ratelimiter_lite.base import BaseRateLimiter


class FixedWindowRateLimiter(BaseRateLimiter):
    """only valid in"""

    def __init__(self, limit: int, period: float):
        super().__init__(limit, period)
        self._counter = 0
        self._last_reset = time.monotonic()
        self._lock = threading.Lock()

    def allow(self) -> bool:
        with self._lock:
            now = time.monotonic()

            if now - self._last_reset >= self._period:
                self._counter = 0
                self._last_reset = now

            if self._counter < self._limit:
                self._counter += 1
                return True

            return False
