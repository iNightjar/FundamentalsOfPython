def list_cpy(list):
    result = []
    for item in list:
        result += [item]

    return result


def main():
    # a and b are distict lists that contains the same elements
    a = [10, 20, 30, 40]
    b = list_cpy(a)  # make a copy

    print('a  = ', a, '  b  = ', b)

    print('Is ', a, ' equals to ', b, ' ? ', sep=' ', end=' ')
    print(a == b)

    print('Are ', a, ' and ', b, ' aliases ? ', sep=' ', end=' ')
    print(a is b)

    b[2] = 35  # change an element of b
    print('a = ', a, ' b = ', b)


main()
