#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print functions from calculator"""
    import calculator_1 as maths

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    elif sys.argv[2] == '+':
        result = maths.add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
        result = maths.sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
        result = maths.mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
        result = maths.div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))

