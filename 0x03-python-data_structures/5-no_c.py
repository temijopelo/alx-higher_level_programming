#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.transalate({ord(i): None for i in 'cC'})
    return new_string
