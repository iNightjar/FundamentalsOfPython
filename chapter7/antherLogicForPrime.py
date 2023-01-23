# return True for prime numbers
from math import sqrt


def is_prime(number):
    """
    Determines the primality of a given value.
    n an integer to test for primality.
    returns true if is prime; otherwise returns false
    """

    result = True
    root = round(sqrt(number)) + 1
    trail_factor = 2
    while result and trail_factor < root:
        result = (number % trail_factor != 0)  # is it a factor ?
        trail_factor += 1
    return result


def main():
    """
    tests for pirmality each integer from 2 up to a value provided by the user.
    if an integer is prime, it prints it ; otherwise, the number is not printed.
    """
    # 8 .. 8 / 8  = 1 , 8 /1 = 8 >>
    max_value = int(input("Show primes within the max value of= "))
    for iterator in range(2, max_value + 1):
        if is_prime(iterator):
            print(iterator, end=" ")
    print()


main()
