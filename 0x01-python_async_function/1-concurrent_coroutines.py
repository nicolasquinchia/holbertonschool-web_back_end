#!/usr/bin/env python3
"""Execute multiple coroutines
at the same time with async
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function that append delays based on
    the time that a imported function is called

    Args:
        n (int): Times to call the function
        max_delay (int): upper limit of the randomized delay

    Returns:
        List[float]: List of delays on each call
    """
    function_calls = []
    for i in range(n):
        function_calls.append(asyncio.create_task(wait_random(max_delay)))

    delay_list = []
    for delay in asyncio.as_completed(function_calls):
        task = await delay
        delay_list.append(task)

    return delay_list
