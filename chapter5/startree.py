# Get tree height from user
height = int(input("Enter height fo tree: "))  # 1

# Draw one row for every unit of height
row = 0  # 1,0
while row < height:  # 0,1
    # print leading spaces, as number of rows gets better
    # leading spaces gets smaller.
    count = 0
    # inner loop 1 to print spaces
    while count < height - row:  # count = 0 , height =1, count = 1 , height = 1
        print(end=' ')  # printed("  ")
        count += 1  # 1,

    # Print out stars, twice    the current row + 1.
    # 1. number of stars on left side of tree
        #  = current row value
    # 2. Exactly one star in the center of tree
    # 2. Number of stars on right side of the tree
        # = current row value
    count = 0  # count =0 , height =1 , row = 0

    # # second inner loop to print *
    while count < 2 * row + 1:
        print(end='*')
        count += 1

    # Move cursor down to next
    print()
    row += 1  # Consider next row
