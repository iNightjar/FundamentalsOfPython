"""Make integers list with while manage exceptions"""


def get_int_in_range(low, high):
    """ Obtains an integer value from the user. Acceptable values
    must fall within the specified range low ... high. """

    val = int(input("input: "))  # can raise a ValueError
    while val < low or val > high:
        print("Value out of range, please try again: ", end=' ')
        val = int(input(""))  # can raise an error

    return val


def create_list(number, min, max):
    """ Allows the user to create a list of n elements consisting
    of integers in the range min ... max"""
    result = []
    while number > 0:  # count down to zoro
        print("Enter integer in the range {} .. {}: ".format(min, max), end=' ')
        result.append(get_int_in_range(min, max))
        number -= 1
    return result


def main():
    """Create a list of two elements suppplied by the user, 
    each element in the range 10 .. 20 """
    list = create_list(2, 10, 20)
    print("Your Created List is : ", list)


if __name__ == '__main__':
    main()  # Invoke main
