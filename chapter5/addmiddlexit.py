# allow the user to enter a sequence of nonnegative
# numbers, the user ends the list with a negative
# number. At the end the sum of the nonnegative numbers is displayed.
# the program prints zero if the user provides no nonegative  numbers


entry = 0
sum = 0

# request input from the user
print("Enter numbers numbers to sum, negative numbers to end the list. ")

while True:
    entry = int(input())
    if entry < 0:
        break
    sum += entry
    print("New sum ==>> ", sum)

print("\n Final sum is equal to: ", sum)
