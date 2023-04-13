# sum the values in a text file containing integer values
try:
    file = open('mydata.dat')

except OSError:
    print("Could not open file. check if file exists please!")

else:  # file opened properly
    sumElements = 0
    try:
        for number in file:
            individualNumber = [int(iterator) for iterator in number.split()]
            sumElements += sum(individualNumber)
    except Exception as error:
        print(error)
        file.close()    # close the file if exception

    print("Sum of integers:", sumElements)
