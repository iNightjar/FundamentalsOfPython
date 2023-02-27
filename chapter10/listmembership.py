list = list(range(0, 21, 2))

for iterator in range(-2, 23):
    if iterator in list:
        print(iterator, ' is a member of ', list)
    if iterator not in list:
        print(iterator, ' is NOT a member of ', list)
