# add numbers to sum

entry = 0
sum = 0

while entry >= 0:
    print(sum)
    entry = int(input("enter number to add sum. negatives ends the list. "))
    if entry >= 0 :
        sum += entry

print('total sum:', sum)
