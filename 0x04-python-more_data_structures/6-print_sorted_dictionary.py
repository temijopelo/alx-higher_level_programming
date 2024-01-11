#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys """

    [print("{:s}: {:s}".format(key, a_dictionary[key])) for key in sorted(a_dictionary)]
