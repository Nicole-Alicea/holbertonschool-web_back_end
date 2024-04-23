#!/usr/bin/env python3
'''Will define and annotate the following variables'''


def variable_annotations():
    '''Defining and annotating the following variables with the
    specified values'''

    a: int
    pi: float
    i_understand_annotations: bool
    school: str

    a = 1
    pi = 3.14
    i_understand_annotations = True
    school = "Holberton"

    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print("i_understand_annotations is a {} with a value of {}"
          .format(type(i_understand_annotations), i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))
