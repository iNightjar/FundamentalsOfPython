from math import sqrt


def is_prime(number):
    """returns true if nonnegative integer number is prime;
    otherwise, returns false"""

    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    trial_factor = 3
    root = sqrt(number)
    while trial_factor <= root:
        if number % trial_factor == 0:
            return False
        trial_factor += 1
    return True


def prime_sequence(begin, end):
    """ generates the sequence fo prime numbers between begin and end."""
    for value in range(begin, end+1):
        if is_prime(value):
            yield value


def main():
    """make a list from generator"""
    primes = list(prime_sequence(20, 50))
    # build the list of prime numbers in the range 20 to 50primes =  list

    print(primes)


if __name__ == '__main__':
    main()  # run the program
