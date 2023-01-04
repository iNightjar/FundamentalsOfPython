# List the factors of the integers 1 .. MAX
# max will be 5 for example
max = 5
# start with base number 1
for iterator in range(1, max + 1):
    factor = 1
    print(end=str(iterator) + ": ")
    for factor in range(1, iterator + 1):
        if iterator % factor == 0:
            print(factor, end=' ')
        factor += 1
    iterator += 1
    print("\nWathcing the baseNumber value: ", iterator)
    print("Wathcing the factor value: ", factor)
    print()
