#!/usr/bin/python3
""" a class to define a size of square """


square1 = __import__("1-square").Square


class Square(square1):
    """ a class to defin and calculate area of the square
    Args:
        square1 (class): a class which define a square with size
    """

    def __init__(self, size=0):
        """initiationing square
        Args:
            size (int): the size of the square passed. Defaults to 0.
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        square1.__size = size
        self.__size = square1.__size

        if type(square1.__size) != int:
            raise TypeError('size must be an integer')
        elif square1.__size < 0:
            raise ValueError('size must be >= 0')
