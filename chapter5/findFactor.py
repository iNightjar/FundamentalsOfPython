# List the factors of the integers 1 .. MAX
# max is 20
max = int(input("Please Enter Integer Limit Number to reach: "))
baseNumber = 1  # start with 1
while baseNumber <= max:
    factor = 1
    print(end=str(baseNumber) + ': ')
    while factor <= baseNumber:
        if baseNumber % factor == 0:
            print(factor, end=' ')
        factor += 1

    baseNumber += 1
    print("\nWathcing the baseNumber value: ", baseNumber)
    print("Wathcing the factor value: ", factor)
    print()
