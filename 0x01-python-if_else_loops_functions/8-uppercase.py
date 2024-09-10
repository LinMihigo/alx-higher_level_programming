#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            newstr += chr(ord(s) - 32)
        else:
            newstr += s
    print("{:s}".format(newstr))
