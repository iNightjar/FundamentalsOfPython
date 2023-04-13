def non_neg_int(number):
    """ converts arguement n into nonnegative integer, if possible.
    Raises a ValueError if the arguement is not convertible to a nonnegative integer. """

    result = int(number)
    if result < 0:
        raise ValueError(result)
    return result


while True:
    try:
        nonNegativeNumber = non_neg_int(
            input("Please enter a nonnegative integer: "))
        if nonNegativeNumber == 999:
            break
        print("You entered: ", nonNegativeNumber)
    except ValueError:
        print("The value you entered is not acceptable. ")
        # raise Exception("Cannot add non-integer to restricted list.")
