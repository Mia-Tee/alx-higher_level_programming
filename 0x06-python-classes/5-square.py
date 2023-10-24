#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents the square
    Attributes:
        __size (int): side of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates  square's area
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size >= 0")
            else:
                self.__size = value

    def my_print(self):
        """print the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
