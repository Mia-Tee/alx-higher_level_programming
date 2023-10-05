#!/usr/bin/python3
# 2-print_alphabet.py

"""Printing the alphabet in lowercase, not following a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")

