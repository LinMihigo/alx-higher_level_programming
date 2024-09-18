#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for item in list(set(my_list)):
        result += item
    return result
