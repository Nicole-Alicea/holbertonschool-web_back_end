#!/usr/bin/env python3
'''The following is a type-annotated function'''


def concat(str1: str, str2: str):
    '''Type-annotated function that takes a string (str1) and a
    string (str2) as arguments and returns a concatenated string'''

    result: str
    result = str1 + str2

    return result
