from sys import argv
from math import sqrt


if len(argv) < 3:
    print("supply range of values")
else:
    for iterator in range(int(argv[1]), int(argv[2]) + 1):
        print(iterator, sqrt(iterator))
    print()
