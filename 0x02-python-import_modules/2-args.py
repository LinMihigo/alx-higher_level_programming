#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguments:".format(len(sys.argv) - 1))
    if len(sys.argv) > 0:
        for i in range(len(sys.argv)):
            if i > 0:
                print("{}: {}".format(i, sys.argv[i]))
