#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finding all multiples of two"""
    a = list()
    for i in my_list:
        if i % 2 == 0:
            a.append(True)
            """leaves no remainder"""
        else:
            a.append(False)
            """leaves a remainder"""
    return a
