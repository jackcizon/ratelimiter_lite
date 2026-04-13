class BaseRateLimiter:  # pragma: no cover
    """single-process rate limiting"""

    def __init__(self, limit: int, period: float) -> None:
        """
        This is a state machine that maintains ratelimiter invariants.

        Rate limiter algorithms are widely used, but they are not difficult to implement.

        The algorithm for a rate limiter is much simpler than that for a red-black tree,
        if you have implemented a red-black tree before.
        """
        self._limit = limit
        self._period = period

    def allow(self) -> bool:
        """
        Do Not Use `__call__`.

        e.g: A ratelimiter prototype via `__call__`.

        class ratelimiter:
            def __init__(self, func: Callable = None, limit=2, period=1.0):
                self._func = func
                self._counter = 0
                self._last_reset = time.monotonic()
                self._lock = threading.RLock()
                self._limit = limit
                self._period = period

            def __call__(self, *args, **kwargs):
                with self._lock:
                    now = time.monotonic()
                    if now - self._last_reset >= self._period:
                        self._counter = 0
                        self._last_reset = now
                    if self._counter >= self._limit:
                        print(">>> [Rate Limited!]")
                        raise Exception
                    self._counter += 1
                return self._func(*args, **kwargs)


        @ratelimiter(limit=3, period=0.5)
        def aaa(args):
            print(args)
            time.sleep(0.1)

        issues:
            1. limiter params cannot change.
            2. where is the function?(can slove it by writing function into `__call__`)
            3. if write function into `__call__`, the code logic is bad.

        If you cram all your algorithmic logic into `__call__`,
        your code will become increasingly bloated.

        click internal uses class to define Command, Parameter, etc....
        then use a wrapper function, like commond(args, ...) factory,
        used by decorator @commond()
        """
        raise NotImplementedError
