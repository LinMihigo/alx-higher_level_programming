#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 1:
        print("{} arguments.".format(len - 1))
    elif len == 2:
        print("{} argument:".format(len - 1))
        for i in range(len):
            if i > 0:
                print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(len - 1))
        for i in range(len):
            if i > 0:
                print("{}: {}".format(i, sys.argv[i]))
