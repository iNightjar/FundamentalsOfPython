# sum values in a text file containing integers
try:
    sumElements = 0
    with open('mydata.dat') as file:
        try:
            for number in file:
                individualReadLine = [int(iterator) for iterator in number.split()]
                # print("list of integers: ", individualReadLine)
                sumElements += sum(individualReadLine)
                # individualReadLine
            print(" Sum of elements: ", sumElements)
        except Exception as error:
            print(error) # show the problem
except OSError: 
    print("could not find file needed!")
finally:
    print("END!")
