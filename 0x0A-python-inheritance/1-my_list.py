#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created

@author: temi
"""


class MyList(list):
    """
     class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        print(sorted(self))
