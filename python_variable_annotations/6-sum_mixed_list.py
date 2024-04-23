#!/usr/bin/env python3
'''The following is a type-annotated function'''

from typing import List


Vector = List[int, float]


def sum_mixed_list(mxd_lst: Vector) -> float:
    '''Type-annotated function that takes a mixed list of integers and
    floats as argument and returns their sum as a float'''

    return float(sum(mxd_lst))
