#!/usr/bin/env python3
'''Annotations for function.'''

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    '''Zoom in on a list of integers by a given factor.'''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
