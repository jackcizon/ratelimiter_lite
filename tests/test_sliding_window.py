import time
from concurrent.futures.thread import ThreadPoolExecutor

from ratelimiter_lite.factory import ratelimiter_factory
from ratelimiter_lite.sliding_window import SlidingWindowRateLimiter


@ratelimiter_factory(SlidingWindowRateLimiter, limit=2, period=0.5)
def task(args):
    print(f"task: {args}")


def test_sliding_window():
    # limit worker count，observe ratelimiter functions.
    with ThreadPoolExecutor(max_workers=5) as p:
        period = 2.0
        start = time.monotonic()
        while True:
            if time.monotonic() - start > period:
                break

            p.submit(task, "running.")
            # wait thread for a while, the period should less than limiter's `period/limit`
            time.sleep(0.05)
