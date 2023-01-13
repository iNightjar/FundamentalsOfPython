from math import sqrt

max_value = int(input("Dsiplay primes up to what value? "))
value = 2  # smallest prime number


while value <= max_value:
    # see if value is prime
    is_prime = True
    iterator = 2
    rootOfValue = sqrt(value)
    while iterator <= rootOfValue:
        # check modules to see if prime
        print(rootOfValue)
        if value % iterator == 0:
            is_prime = False
            break
        iterator += 1

    if is_prime:
        print(value, end=' ')
    value += 1

print()
