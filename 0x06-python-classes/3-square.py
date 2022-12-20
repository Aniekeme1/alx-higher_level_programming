#!/usr/bin/python3
""" a class to define a size of square """


class Square():
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
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ finding the area of the square
        Returns:
            int: the are of the square
        """
        return self.__size**2
