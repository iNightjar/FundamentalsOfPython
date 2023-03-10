list = [1, 2, 3, 4, 5, 6, 7, 8]

print('prefixs of ', list)
for iterator in range(0, len(list) + 1):
    print('<', list[0:iterator], '>', sep='')

print()
print('---------------------')
print()

print('suffixes of ', list)
for iterator in range(0, len(list) + 1):
    print('<', list[iterator:len(list) + 1], '>', sep='')
