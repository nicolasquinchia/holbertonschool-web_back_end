#!/usr/bin/env python3
"""The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Delay based on a random interval

    Args:
        max_delay (float, optional): upper limit of the delay. Defaults to 10.

    Returns:
        float: Delay excecuted in the asynchronous coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
