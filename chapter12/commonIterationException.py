sumElements  = 0
list = [1,2,4,5]
iterator = 0
try:
    while True:
        sumElements += list[iterator]
        iterator += 1
except IndexError as error:
    print(error)
    pass
print("Sum = ", sumElements)