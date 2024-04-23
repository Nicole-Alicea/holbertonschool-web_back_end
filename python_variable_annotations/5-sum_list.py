#!/usr/bin/env python3
'''The following is a type-annotated function'''

from typing import List


Vector = List[float]


def sum_list(input_list: Vector) -> float:
    '''Type-annotated function that takes a list of floats as argument
    and returns their sum as a float'''

    return float(sum(input_list))
