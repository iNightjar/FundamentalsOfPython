from math import sqrt


def squareRoot(value):
    """ compute an approximation of the square root of x    """
    # compute a provisional  sqaure root
    root = 1.0

    # how far off is our provisional root
    diff = root * root - value

    while diff > 0.00000001 or diff < -0.00000001:
        root = (root + value/root) / 2
        diff = root * root - value
    return root


def main():
    d = 1.0

    while d <= 10.0:
        print('{0:6.1f}: {1:16.8f} {2:16.8f}' \
            .format(d, squareRoot(d), sqrt(d)))

        d += 0.5


main()
