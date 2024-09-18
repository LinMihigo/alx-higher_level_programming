#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    maxi = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v == maxi:
            return k
