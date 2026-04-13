Rate Limit Components
==================================

.. image:: https://github.com/jackcizon/ratelimiter_lite/actions/workflows/ci.yaml/badge.svg
   :target: https://github.com/jackcizon/ratelimiter_lite/actions/workflows/ci.yaml/badge.svg
   :alt: CI


**version: 0.1.4**

.. code-block:: shell

   pip install ratelimiter_lite

Demo Usage:
----------------

.. code-block:: python

   import time
   from concurrent.futures.thread import ThreadPoolExecutor

   from ratelimiter_lite.factory import ratelimiter_lite_factory
   from ratelimiter_lite.fixed_window import FixedWindowratelimiter


   @ratelimiter_factory(FixedWindowratelimiter, limit=2, period=0.3)
   def task(args):
      print(f"task: {args}")


   def test_fixed_window():
      # limit worker count，observe ratelimiter_lite functions.
      with ThreadPoolExecutor(max_workers=5) as p:
         period = 2.0
         start = time.monotonic()
         while True:
               if time.monotonic() - start > period:
                  break

               p.submit(task, "running.")
               # wait thread for a while, the period should less than limiter's `period/limit`
               time.sleep(0.05)
