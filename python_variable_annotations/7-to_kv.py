#!/usr/bin/env python3
'''The following is a type-annotated function'''

import math


def to_kv(k: str, v: int | float) -> tuple:
    '''Type-annotated function that takes a string and an integer or float
    (v) as arguments and returns a tuple. The first element of the tuple is
    the string and the second element is the square of v.'''

    return (k, float(math.sqrt(v)))
