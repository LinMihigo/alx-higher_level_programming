#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary)
    sorted_keys.sort()
    for key in sorted_keys:
        print("{:s}: {}".format(key, a_dictionary.get(key)))
