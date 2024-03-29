#!/usr/bin/env python3
'''Async Comprehension'''

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''Async Comprehension'''
    return [i async for i in async_generator()]
