#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """
    Attributes:
        __size (int): represents the size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): representa the side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size is integer")
        else:
            if size < 0:
                raise ValueError("size >= 0")
            else:
                self.__size = size

    def area(self):
        """
        Returns:
            Area of a square
        """
        return (self.__size) ** 2
