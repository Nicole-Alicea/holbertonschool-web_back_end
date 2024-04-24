#!/usr/bin/env python3
'''The following is a type-annotated function'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Type-annotated function that takes a string and an integer or float
    (v) as arguments and returns a tuple. The first element of the tuple is
    the string and the second element is the square of v.'''

    return k, float(v * v)
