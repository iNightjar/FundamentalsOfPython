# computes GCD number : the largest common divisor
def gcd(num1, num2):
    # determine the smallest number
    min = num1 if num1 < num2 else num2

    largest_factor = 1
    for iterator in range(1, min + 1):
        if num1 % iterator == 0 and num2 % iterator == 0:
            largest_factor = iterator  # found the larget factor

    return largest_factor


numberOne = int(input("Please Enter the First number: "))
numberTwo = int(input("Please Enter the First number: "))

print("Returning the larget factor: ", gcd(numberOne, numberTwo))
 