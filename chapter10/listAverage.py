def main():
    # set up variables
    sum = 0.0
    number_of_entries = 5
    numbers = []
    # get input from user
    print("please enter: ", number_of_entries, " numbers: ")
    for iteration in range(0, number_of_entries):
        inputEntered = float(input("Enter number " + str(iteration) + ": "))
        numbers += [inputEntered]
        sum += inputEntered
    print()
    print(numbers)
    print()
    print("Avarage: ", sum/number_of_entries)

# print(main())
main()



