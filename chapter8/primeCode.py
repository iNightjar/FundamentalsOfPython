"""contains the definition of the is_prime function"""
from math import sqrt

def is_prime(number):
    """Returns True if the nonnegative integer number is prime; otherwise, returns false"""
    trail_factor = 2
    root= sqrt(number)


    while trail_factor <= root:
        if number % trail_factor == 0 :
            return False
        trail_factor  += 1

    return True

print(is_prime(22))