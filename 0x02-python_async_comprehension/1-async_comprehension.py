#!/usr/bin/env python3
"""[Async Comprehensions]
"""

from typing import List
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[Coroutine called that takes no arguments,
    The coroutine will collect 10 random numbers using
    an async comprehensing over async_generator]

    Returns:
        list[float]: [list of 10 random numbers]
    """
    result = [num async for num in async_generator()]
    return result
