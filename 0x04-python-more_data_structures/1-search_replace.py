#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """a function that replaces all occurrences of an element by another in a new list"""
    return [replace if value == search else value for value in my_list]
