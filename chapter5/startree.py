# Get tree height from user
height = int(input("Enter height fo tree: "))

# Draw one row for every unit of height
row = 0
while row < height:
    # print leading spaces, as number of rows gets better
    # leading spaces gets smaller.
    count = 0
    while count < height - row:
        print(end=' ')
        count += 1

    # Print out stars, twice    the current row + 1.
    # 1. number of stars on left side of tree
        #  = current row value
    # 2. Exactly one star in the center of tree
    # 2. Number of stars on right side of the tree
        # = current row value
    count = 0
    while count < 2 * row + 1:
        print(end='*')
        count += 1

    # Move cursor down to next
    print()
    row += 1  # Consider next row
