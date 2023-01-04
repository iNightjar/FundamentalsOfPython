word = input('Enter Text (No X\'s, Please): ')

"""
Using for/else in iteration ==>> if loop breaked in line:14.. the else portion wouldn't be excuted.
"""

vowelCount = 0
for iterator in word:
    if iterator == 'A' or iterator == 'a' or iterator == 'e' or iterator == 'E' \
            or iterator == 'I' or iterator == 'i' or iterator == 'O' or iterator == 'o':
        vowelCount += 1
    elif iterator == 'X' or iterator == 'x':
        print("X is not allowd.")
        break
else:
    print('(', vowelCount, ' vowels)', sep='', end='')
