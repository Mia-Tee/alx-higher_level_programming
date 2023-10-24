#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the square
        __position (tuple): the position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): side of the square
            position (tuple): the position of the square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates square's area
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
        """prints the defined square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """
        Returns:
            position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): the position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position should be the tuple of 2 positive integers")
        else:
            self.__position = value
