#!/usr/bin/python3

"""Prints all names defined by hidden_4 module."""
if __name__ == "__main__":
    import hidden_4
    for s in dir(hidden_4):
        if s[:2] != "__":
            print("{:s}".format(s))
