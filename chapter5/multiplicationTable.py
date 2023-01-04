# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))

# print a size x size multiplication tabl
for row in range(1, size+1):
    
    # print("Row #", row)
    for column in range(1, size+1):
        product = row * column
        print('{0:4}'.format(product), end=' ')
    print()
