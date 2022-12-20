#!/usr/bin/python3
""" a class to define a size of square """


class Square():
    """ a class to define and calculate area of the square
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
        if type(self.__size) != int and type(self.__size) != float:
            raise TypeError('size must be a number')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        Square.Area = self.__size**2

    @property
    def size(self):
        """getter for size
        Returns:
            integer: sends the value of private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size
        Args:
            value (int): a new size value
        Raises:
            TypeError: if not integer
            ValueError: if < 0
        """

        if type(self.__size) != int and type(self.__size) != float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ finding the area of the square
        Returns:
            int: the are of the square
        """
        return self.__size**2

    def __lt__(self, other):
        """less than comparison function
        Args:
            other (instance): another square instance
        Returns:
            boolean: comparison result
        """
        return self.__size < other.__size

    def __le__(self, other):
        """less than or equal to comparison
        Args:
            other (instance): another square instance
        Returns:
            boolean: comparison result
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """ equal to comparison
        Args:
            other (instance): another square instance
        Returns:
            boolean: comparison result
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """not equal to comparison
        Args:
            other (instance): another square instance
        Returns:
            boolean: comparison result
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """greater than comparison
        Args:
            other (instance): another square instance
        Returns:
            boolean: comparison result
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """greater than or equal to comparison
        Args:
            other (instance): another square instance
        Returns:
            boolean: comparison result
        """
        return self.__size >= other.__size
