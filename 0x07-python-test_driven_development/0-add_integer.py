#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""
def add_integer(var, bar=98):
    """ Function that adds two integer and/or float numbers
    Args:
        var: first variable 
        bar: second variable
    Returns:
        The summation of the two given numbers
    Raises:
        TypeError: If var or bar aren't integer and/or float numbers
    """

    if not isinstance(var, int) and not isinstance(var, float):
        raise TypeError("var must be an integer")
    if not isinstance(bar, int) and not isinstance(bar, float):
        raise TypeError("bar must be an integer")
    var = int(var)
    bar = int(bar)
    return (var + bar)
