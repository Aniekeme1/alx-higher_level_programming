#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:01 2022
@author: Aniekeme Umoren
"""


def print_square(size):
    """
    print a square of char #
    Args:
        size (int): size of the square
    Raises:
        TypeError: Exception if size is not integer
        ValueError: Exception if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#'*size)
