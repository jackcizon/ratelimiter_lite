import time
from random import random

from ratelimiter_lite.factory import ratelimiter_factory
from ratelimiter_lite.token_bucket import TokenBucketRateLimiter


@ratelimiter_factory(TokenBucketRateLimiter, limit=5, period=5)
def task(args):
    print(f"task: {args}")
    simulate_execute_time = random()
    time.sleep(simulate_execute_time)


def test_token_bucket():
    # limit worker count，observe ratelimiter functions.
    # with ThreadPoolExecutor(max_workers=1) as p:
    #     period = 1.0
    #     start = time.monotonic()
    #     while True:
    #         if time.monotonic() - start > period:
    #             break
    #
    #         p.submit(task, "running.")
    #         # wait thread for a while, the period should less than limiter's `period/limit`
    #         time.sleep(0.05)
    for i in range(1, 21):
        task(f"running {i}")
