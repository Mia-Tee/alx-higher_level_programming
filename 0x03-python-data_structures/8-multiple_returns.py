#!/usr/bin/python3

def multiple_returns(sentence):
    """return a tuple with the length of a string and its first character"""
    if 0 == len(sentence):
        return 0, None
    return len(sentence), sentence[0]
