#!/usr/bin/python3

def max_integer(my_list=[]):
    """finding the biggest integer of the list"""
    if 0 == len(my_list):
        return None
    return sorted(my_list)[-1]
