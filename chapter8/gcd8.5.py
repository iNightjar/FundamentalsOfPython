def gcd(minn, num):
    """
    Uses Euclid's method to compute the greatest common divisor
    (also called greatest common factor) of min and num.
    returns the GCD of min and num
    """
    if num == 0:
        return minn
    else:
        return gcd(num, minn % num)


def iterative_gcd(number1, number2):
    """uses a naive algorithms to compute the greatest commin divisor
    (also called the greatest common factor) of min and num.
    returns the gcd of min and num.
    """
    # Determine the smaller of number1 and number2
    min = number1 if number1 < number2 else number2
    # 1 is definitely a common factor to all intergers
    largest_factor = 1
    for iterator in range(1, min + 1):
        if number1 % iterator == 0 and number2 % iterator == 0:
            largest_factor = iterator  # found the largest factor
    return largest_factor


def main():
    """try out the gcd function"""
    firstNumber, secondNumber = int(input("Enter number please: ")), int(
        input("Enter number please"))
    for number1 in range(1, firstNumber):
        for number2 in range(1, secondNumber):
            print("gcd of ", number1, " and ", number2,
                  " is ", gcd(number1, number2))


main()
