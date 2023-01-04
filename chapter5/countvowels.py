word = input("enter text: ")
vowel_letterount = 0
for letter in word:
    if letter == 'a' or letter == 'A' or letter == 'E' or letter == 'e' \
            or letter == 'I' or letter == 'i' or letter == 'O' or letter == 'o':
        print(letter, ', ', sep='', end=' ')
        vowel_letterount += 1
print('(', vowel_letterount, ' vowels)', sep='')
