#!/usr/bin/env python3
'''Annotations for callable objects.'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return a function that multiplies a float by multiplier.'''

    def f(n: float) -> float:
        '''Return the product of the float and multiplier.'''
        return n * multiplier

    return f
