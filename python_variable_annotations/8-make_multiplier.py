#!/usr/bin/env python3
'''The following is a type-annotated function'''


def make_multiplier(multiplier: float):
    '''Type-annotated function that takes a float as argument and returns
    a function that multiplies a float by multiplier'''

    return callable([float]*multiplier)
