#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """ returns a set of all elemts present in only a set """
    return ((set_1 | set_2) - (set_1 & set_2))
