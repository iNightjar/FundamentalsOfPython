count = sum = 0
print("Please provide five nonnegative numbers when prompted. ")
while count < 5:
    # Get value from the user
    entry = float(input("Enter numbers: "))
    if entry < 0:
        print("negative numbers not acceptable! Terminating ")
        print('Avarage is: ', sum/count)
        break
    sum += entry
    count += 1

print('Avarage is: ', sum/count)
