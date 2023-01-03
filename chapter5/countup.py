# counts up from zero, the user continues the count by entering
# 'Y'. the user discountinues the count by entering 'N'

count = 0
entry = 'Y'

while entry != 'n' or entry != 'N':
    # print the current value of count
    print(count)
    entry = input('Please enter "Y" to continue the count or "N" to quit: ')
    if entry == 'Y' or entry == 'y':
        count += 1  # keep counting
    elif entry != 'n' or entry != 'N':
        print('"', entry, '"', "is not a valid choice. ")
        break
