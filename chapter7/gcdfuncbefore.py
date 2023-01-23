def get_numbers():
    numberOne = int(input("Please enter an integer value: "))
    numberTwo = int(input("Please enter an integer value: "))
    return numberOne, numberTwo


def gcd(numberOne: int, numberTwo: int) -> int:  # return value INTEGER
    # determine which one is smaller
    min = numberOne if numberOne < numberTwo else numberTwo

    largest_factor = 1
    for iterator in range(1, min+1):
        if numberOne % iterator == 0 and numberTwo % iterator == 0:
            largest_factor = iterator

    print(largest_factor)


def main():
    n1, n2 = get_numbers()
    gcd(n1, n2)


main()
