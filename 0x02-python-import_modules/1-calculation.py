#!/usr/bin/python3

if __name__ == "__main__":
    """Print maths"""
    import calculator_1 as maths

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, maths.add(a, b)))
    print("{} - {} = {}".format(a, b, maths.sub(a, b)))
    print("{} * {} = {}".format(a, b, maths.mul(a, b)))
    print("{} / {} = {}".format(a, b, maths.div(a, b)))
