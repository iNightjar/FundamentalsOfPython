from random import randrange


def max(num1, num2):
    """ determine the maximum of two numbers"""
    call_string = "max({}, {})".format(num1, num2)
    print(">>> Calling ", call_string)
    result = num1 if num1 > num2 else num2
    print("<<< Returning {} format from ".format(result) + call_string)

    return result


# This time just call the functions, and let each function print its
# parameter and result details.

max(20, 30)
print("---------------------------")
max(30, 20)
