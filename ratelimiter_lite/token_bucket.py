import threading
import time

from ratelimiter_lite.base import BaseRateLimiter


class TokenBucketRateLimiter(BaseRateLimiter):
    def __init__(self, limit: int, period: float):
        super().__init__(limit, period)
        self._capacity = limit
        self._tokens = limit
        self._rate = limit / period
        self._last_time = time.monotonic()
        self._lock = threading.Lock()

    def allow(self) -> bool:
        with self._lock:
            now = time.monotonic()
            delta_time = now - self._last_time
            new_tokens = delta_time * self._rate

            self._tokens = min(self._capacity, self._tokens + new_tokens)  # type: ignore
            self._last_time = now

            if self._tokens >= 1:
                self._tokens -= 1
                return True
            return False
