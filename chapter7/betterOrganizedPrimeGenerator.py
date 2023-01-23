from math import sqrt


def is_prime(number):
    """
    Determines the primality of a given value.
    n an integer to test for primality.
    returns true if is prime; otherwise returns false
    """
    root = round(sqrt(number)) + 1  # nubmer = 4 > root = 3
    # print(root)
    for trail_factor in range(2, root):
        if number % trail_factor == 0:
            return False
        trail_factor += 1
    return True


def main():
    """
    tests for pirmality each integer from 2 up to a value provided by the user.
    if an integer is prime, it prints it ; otherwise, the number is not printed.
    """

    max_value = int(input("Enter max value to loop for primes: "))
    for iterator in range(2, max_value + 1):
        if is_prime(iterator):  # see if the value is prime
            # return iterator
            print(iterator, end=" ")  # display the prime value
    print()


main()
main()
