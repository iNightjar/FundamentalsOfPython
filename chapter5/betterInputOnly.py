
# require the user to enter an integer in the range 1-10

in_value = 0
attemptes = 0

while in_value < 1 or in_value > 10:
    in_value = int(input("enter an integer in range 0-10: "))
    attemptes += 1

# Make singular or plural word as necessary
tries = "try" if attemptes == 1 else "tries"
# in_value at this point is guaranteed to be within range
print("It took you", attemptes, tries, "to enter a valid number")
