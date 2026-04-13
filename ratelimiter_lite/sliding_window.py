import threading
import time
from collections import deque

from ratelimiter_lite.base import BaseRateLimiter


class SlidingWindowRateLimiter(BaseRateLimiter):
    def __init__(self, limit: int, period: float):
        super().__init__(limit, period)
        self._log: deque[float] = deque()
        self._lock = threading.Lock()

    def allow(self) -> bool:
        with self._lock:
            # `now - self._period` calculates the lower bound
            # (the earliest valid timestamp) of the current sliding window
            now = time.monotonic()
            low_bound = now - self._period

            # log[0] represents the earliest access record.
            # If this earliest access record is less than the earliest access point in the current interval,
            # it should be deleted.
            while self._log and self._log[0] <= low_bound:
                self._log.popleft()

            visited_size = len(self._log)
            if visited_size < self._limit:
                self._log.append(now)
                return True

            return False
