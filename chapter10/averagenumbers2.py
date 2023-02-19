def main():
    sum = 0.0
    number_of_entries = 5

    print("please enter", number_of_entries, " numbers: ")
    for iterator in range(0, number_of_entries):
        num = float(input("Enter number " + str(iterator) + ": "))
        sum += num
    print("Average: ", sum/number_of_entries)

main()
