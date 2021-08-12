#!/usr/bin/env python3
"""Tasks file, task_wait_random"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[Multiple coroutines at the same time with async]
    Args:
        n (int): [Number of iterations]
        max_delay (int): [Delay value, defaults to 10]
    Returns:
        list: [List of all the delays]
    """
    calls = []
    for i in range(n):
        calls.append(task_wait_random(max_delay))

    list_delays = []
    for delay in asyncio.as_completed(calls):
        tasks = await delay
        list_delays.append(tasks)

    return list_delays
