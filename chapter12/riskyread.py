sumElements = 0
with open('mydata.dat') as file:
    for number in file:
        individualNumber = [int(iterator) for iterator in number.split()]
        sumElements += sum(individualNumber)

print(sumElements)
 