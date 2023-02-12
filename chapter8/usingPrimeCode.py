from primeCode import is_prime

number = int(input("Enter an integer: "))
if is_prime(number):
    print(number, " is prime")
else:
    print(number, " is NOT prime")
