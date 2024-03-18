#!/usr/bin/env python3

"""A simple example of using async/await syntax in Python 3.7+."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of time between 0 and `max_delay`."""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
