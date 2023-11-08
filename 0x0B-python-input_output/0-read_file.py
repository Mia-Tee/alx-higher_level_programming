#!/usr/bin/python3
"""This module reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """this prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
