#!/usr/bin/env python3
'''Measure the runtime'''


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure the runtime'''
    import time
    import asyncio

    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end = time.time()
    return end - start
