#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            print("{}".format(chr(ord(s) - 32)), end='')
        else:
            print("{}".format(s), end='')
    print()
