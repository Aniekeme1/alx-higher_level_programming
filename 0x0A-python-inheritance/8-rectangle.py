#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed 11th Jan 2023
@author: Aniekeme Umoren
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inheirts from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
