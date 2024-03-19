#!/usr/bin/env python3
'''Asynchronous Generator'''


async def async_generator():
    '''Asynchronous Generator'''
    import asyncio
    import random

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
