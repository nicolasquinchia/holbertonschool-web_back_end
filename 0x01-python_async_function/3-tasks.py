#!/usr/bin/env python3
"""Task file
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[Function that create a asyncio task]

    Args:
            max_delay (int): [Delay value, defaults to 10]

    Returns:
            syncio.Task: [Function asyncio task]
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
