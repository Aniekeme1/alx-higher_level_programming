#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Tue Jan 10th, 2023
=======
Created on Mon jan 9th 2023
>>>>>>> 2032be9f271d143a323d0e19470641cb57395d26
@author: Aniekeme Umoren
"""


class BaseGeometry():
    """
    An empty class
    """
    pass

    def area(self):
        """
        Public instance method that calculates the area
        Raises:
            Exception if area is not imlemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates integer input
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
