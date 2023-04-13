def non_neg_int(number):
    result = int(number)
    if result < 0:
        raise ValueError(result)
    return result


while True:
    nonNegativeNumber = non_neg_int(
        input("Please enter a nonnegative integer: "))
    if nonNegativeNumber == 999:
        break

    print("You entered: ", nonNegativeNumber)
