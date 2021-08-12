#!/usr/bin/env python3
"""Measure the runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[Function that measures the total
        execution time for wait_n]
    Args:
        n (int): [Number of iterations]
        max_delay (int): [Delay value, defaults to 10]
    Returns:
        float: [Total time of execution]
    """

    first_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    second_time = time.time()
    total_time = (second_time - first_time)
    return total_time / n
