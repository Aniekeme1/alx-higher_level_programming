#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon 9th Jan 2023
@author: Aniekeme Umoren
"""


def is_same_class(obj, a_class):
    """
    Checks if two objects are the same class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)
