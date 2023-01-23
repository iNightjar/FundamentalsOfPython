def get_int_in_range(first, last):
    """
    Forces the user to enter an integer within a specified range.
    first is either a minimum or maximun accpetable value.
    last is the corresponding other end of the range, either a maximum or minimun value
    returns an accepteable value from the user.
    """
    # if the larger number is provided first,
    # switch the parameters.

    if first > last:
        first, last = last, first

    # insist on values in the range first ... last
    in_value = int(input("Please enter values in the range "
                         + str(first) + " .... " + str(last) + " : "))

    while in_value < first or in_value > last:
        print(in_value, " is not in the range", first, "...", last)
        in_value = int(input("Please try again: "))
        # in_value at this point is gruanteed to be within the range

    return in_value


def main():
    """Tests the get_int_in_range function"""
    print(get_int_in_range(23, 2))

main()
