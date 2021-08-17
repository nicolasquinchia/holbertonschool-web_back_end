#!/usr/bin/env python3
"""[Async Generator]
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """[Coroutine called that takes no arguments,
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second]

    Yields:
        Generator[float, None, None]:
        [List of random numbers between 0 and 10]
    """
    for index in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
