#!/usr/bin/env python3
'''TypeVar module'''

from typing import Any, TypeVar, Mapping, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    '''Safe get value from dictionary.'''
    if key in dct:
        return dct[key]
    else:
        return default
