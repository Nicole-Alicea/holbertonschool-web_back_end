#!/usr/bin/env python3
'''The following is a type-annotated function'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Type-annotated function'''

    return [(i, len(i)) for i in lst]
