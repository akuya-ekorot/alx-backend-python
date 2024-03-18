#!/usr/bin/env python3

"""Running concurrent coroutines"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of the delays in ascending order.
    """

    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
