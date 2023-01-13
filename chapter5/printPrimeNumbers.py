# printing prime numbers
# prime nubmer is an integer greater thatn one whose only factors (also called divisors) are the one and itself.


# primes until max_value
primeNumber = int(input("Display primes up to what value: "))

value = 2
# 9 is odd but not prime
while value <= primeNumber:  # loop until the max value
    is_prime = True
    iteratorInsideValue = 2
    while iteratorInsideValue < value:
        if value % iteratorInsideValue == 0:
            is_prime = False  # Factor is found, Not Prime Number
            break
        iteratorInsideValue += 1

    if is_prime:  # only print value when True bool result from the inner while loop
        print(value, end=" ")
    value += 1
print()  # move the cursor down to next line
