from math import fabs


def equality(a, b, tolerance):
    return a == b or fabs(a - b) < tolerance


def main():
    i = 0.0
    while not equality(i, 1.0, 0.00001):
        print("i = ", i)
        i += 0.1


main()
