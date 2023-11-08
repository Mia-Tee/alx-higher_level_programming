#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """rebel version of an integer"""
    def __eq__(self, other):
        """what was previously != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was previously == is now !="""
        return int(self) == other
