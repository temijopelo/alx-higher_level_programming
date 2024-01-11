#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """ updates or add key into a dictionary """

    a_dictionary.update({key:value})
    return (a_dictionary.copy())
