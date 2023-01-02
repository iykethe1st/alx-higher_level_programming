#!/usr/bin/python3

"""
    Simple "Add Integer" module.
"""

def add_integer(a, b=98):
    """ Adds "a" and "b"
    args:
        a: first argument
        b: second argument
    raises:
        TypeError: if a or b is neither integer nor float
    note:
        a and b must be first casted to integers if they are float
    """

    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b        
