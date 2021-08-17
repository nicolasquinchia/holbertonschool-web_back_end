#!/usr/bin/env python3
"""Run time for four parallel comprehensions
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[Coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather and
    measure the total runtime]

    Returns:
        float: [Total runtime]
    """

    first_time = time.time()
    result = await asyncio.gather(*(async_comprehension() for i in range(4)))
    second_time = time.time()
    total_time = (second_time - first_time)
    return total_time
