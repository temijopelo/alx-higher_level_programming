#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ replaces all occurences"""

    swap = [swp if swp != search else replace for swp in my_list]

    return swap
