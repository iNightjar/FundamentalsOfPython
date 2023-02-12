# contains the definition of the is_prime function
from math import sqrt


def is_prime(number):
    """Returns True if nonnegative integer n is prime;
    otherwise, returns false"""

    if number == 2:  # 2 is the only even prime number
        return True
    if number < 2 or number % 2 == 0:  # handle simple cases immediately
        return False
    trial_factor = 3
    root = sqrt(number)
    while trial_factor <= root:
        if number % trial_factor == 0:
            return False
        trial_factor += 1

    return True


def prime_squence(begin, end):
    """Generate the sequence of prime numbers between begin and end. """
    for value in range(begin, end + 1):
        if is_prime(value):
            yield value


def main():
    """ Experiments with the prime number generator"""
    min_value = int(input("Enter start of range: "))
    max_value = int(input("Enter last of range: "))

    print("Print all the primes from", min_value, " to ", max_value)
    for value in prime_squence(min_value, max_value):
        print(value, end=" ")  # display the prime number
    print()

    print("Print all the primes in that range that end with digit(3)")
    for value in prime_squence(min_value, max_value):
        if value % 10 == 3:  # see if value's ones digit is 3
            print(value, end=" ")
    print()

    # add up all the primes in the range
    sum = 0
    for value in prime_squence(min_value, max_value):
        sum += value
    print("The sum of the primes in that range is : ", sum)

    # decorate the output
    print("Fancier display")
    for value in prime_squence(min_value, max_value):
        print('<' + str(value) + '>', end=" ")


if __name__ == '__main__':
    main()  # run the program


