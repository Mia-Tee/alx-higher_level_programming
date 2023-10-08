#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of the list in reverse order"""
    if not my_list:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i))
