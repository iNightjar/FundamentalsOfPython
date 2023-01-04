# using all INT even the entry

print("Please enter positive number to add for sum or negative number to exit:", end=' ')

entry = 0
sum = 0
while entry >= 0:
    entry = int(input())
    if entry >= 0:
        sum += entry
        print(sum)
print("Total sum = ", sum)
