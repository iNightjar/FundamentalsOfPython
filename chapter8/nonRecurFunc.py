def factorial(number):
    """
    compute number!
    returns the factorial of number
    """
    product = 1
    while number:
        product *= number
        number -= 1
    return product


def main():
    """try out the factorial function"""
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 6! = ", factorial(6))
    print(" 10! = ", factorial(10))


main()
