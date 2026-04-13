from collections.abc import Callable
from functools import wraps
from typing import Any

from ratelimiter_lite.base import BaseRateLimiter


def ratelimiter_factory[T: BaseRateLimiter](cls: type[T], limit: int, period: float) -> Callable:
    limiter = cls(limit, period)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable | None:
            if limiter.allow():
                return func(*args, **kwargs)
            else:
                print(f"[{func.__name__}] Rate limit exceeded")
                return None

        return wrapper

    return decorator
