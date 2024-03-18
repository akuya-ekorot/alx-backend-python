#!/usr/bin/env python3

'''Annotation for Tuples'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuple with a string and a float.'''
    return (k, v ** 2)

