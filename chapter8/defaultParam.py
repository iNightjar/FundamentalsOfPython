number = int(input("Enter a number please: "))
#  count down from number provided to zero


def countToNumber(number=10):
    for iterator in range(number, -1, -1):
        print(iterator)


countToNumber()
