# Get the value from user
value = float(input("Enter number: "))
# compute the provisional square root
root = 1.0

# how for off is our provisional root ?
diff = root * root - value
# loop until the provisional root
# is close enough to the actual root
while diff > 0.00000001 or diff < - 0.00000001:
    print(root, 'square is ', root*root)  # report how we are doing

    root = (root + value/root) / 2  # compute new provisional root
    # how bad our current approximation ?
    diff = root * root - value

# report approximation square root
print('Square root of ', value, ' = ', root)
