#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed 11th Jan 2023
@author: Aniekeme Umoren
"""


def pascal_triangle(n):
    """
    Creates a pascal triangle
    Attributes:
        n (int): The n exponent for triangle
    Return:
        A matrix with values for the triangle
    """
    pascal = []
    triangle = []

    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        pos = len(pascal)
        for i in range(1, pos):
            new[i] = pascal[i - 1] + pascal[i]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
