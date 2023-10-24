#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): represents the size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of the size
        Args:
            value (int): size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size is integer")
        else:
            if value < 0:
                raise ValueError("size >= 0")
            else:
                self.__size = value
