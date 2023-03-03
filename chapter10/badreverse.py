def make_list():
    """
    builds a list from input provided by the user
    """

    result = []
    in_val = 0
    while in_val >= 0:
        in_val = int(input("Enter valid positive numbers only: "))
        if in_val >= 0:
            result = result + [in_val]
    return result

def main():
    # hello inside the main function
    revers = make_list()
    # print the list in reverse
    for iterator in range(len(revers) -1, -1, -1):
        print(revers[iterator], end=' ')
    print()

main()
