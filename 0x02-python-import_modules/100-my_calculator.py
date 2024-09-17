#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if len(args) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        if args[2] == '+':
            print("{} {} {} = {}".format(a, args[2], b, add(a, b)))
        elif args[2] == '-':
            print("{} {} {} = {}".format(a, args[2], b, sub(a, b)))
        elif args[2] == '*':
            print("{} {} {} = {}".format(a, args[2], b, mul(a, b)))
        elif args[2] == '/':
            print("{} {} {} = {}".format(a, args[2], b, div(a, b)))
        else:
            str = "Unknown operator. Available operators: +, -, * and /"
            print("{}".format(str))
            sys.exit(1)
