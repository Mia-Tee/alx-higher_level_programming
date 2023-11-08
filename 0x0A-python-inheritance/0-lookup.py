#!/usr/bin/python3
"""
    This function will return the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """This function returns a list of all the available attributes and methods of an object"""
    return dir(obj)
