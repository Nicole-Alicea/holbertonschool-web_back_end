#!/usr/bin/env python3
'''The following is a type-annotated function'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Type-annotated function that takes a float as argument and returns
    a function that multiplies a float by multiplier'''

    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
