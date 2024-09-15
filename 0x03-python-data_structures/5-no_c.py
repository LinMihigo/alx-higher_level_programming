#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            newstr += char
    return newstr
