#!/usr/bin/env python3
'''Annotations for mixed list function.'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Return the sum of the mixed list.'''
    return sum(mxd_lst)
