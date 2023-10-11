#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """a function that replaces all occurrences of an element by another in a new list"""
    def find_search(element):
        return element if element != search else replace
    return list(map(find_search, my_list))
