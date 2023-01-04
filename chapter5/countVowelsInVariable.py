variable = input("Enter text (no X\'s, please): ")
sumOfIterators = 0
for iterator in variable:
    if iterator == 'a' or iterator == 'i' or iterator == 'o' \
            or iterator == 'e':
        print('(', iterator, ')', sep='', end='')  # print the vowel itself
        sumOfIterators += 1
    elif iterator == 'X' or iterator == 'x':
        break  # exit while looping

print('\n( ', sumOfIterators, ' vowels )', sep='')
