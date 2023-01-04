#  Add five nonnegative numbers supplied by the user
count = sum = 0
print('Please provide five nonnegative numbers when prompted')
while count < 5:
    # Get input from the user
    entry = float(input("Enter numbers: "))
    if entry < 0:
        break
    count += 1
    sum += entry

if count < 5:
    print("Negative numbers not acceptable! Terminating.")
else:
    print("Avarage:", sum/count)
