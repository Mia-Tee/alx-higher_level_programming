#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """printing a matrix of integers"""
    for row in matrix:
        for column in row:
            print("{:d}".format(column), sep='', end='')
            if (column != row[len(row) - 1]):
                print(' ', end='')
        print()
