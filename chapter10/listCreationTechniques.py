list0 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

list1 = []
for iterator in range(2, 21, 2):
    list1 += [iterator]
print(" simple list creation :: ", list1)

# List generator creation
listGenerator = list(range(2, 21, 2))
print(" simple list creation with generator:: ", listGenerator)


# list comprehension
list3 = [x for x in range(1, 21) if x % 2 == 0]
print(" list comprehension creation :: ", list3)


# combination of methods with list concatenation:
listCombination = list(range(2, 9, 2)) + \
    [10, 12, 14] + [x for x in range(16, 21, 2)]
print("list comprehension, compenation with list creation ::  ", listCombination)
