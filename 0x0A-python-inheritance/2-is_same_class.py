#!/usr/bin/python3
"""
This module checks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """returns True if object ( obj) is the exact class a_class, otherwise False"""
    return (type(obj) == a_class)
