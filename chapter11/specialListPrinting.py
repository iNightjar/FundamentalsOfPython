list = [2*iterator for iterator in range(6)]


# typeical list printing

print(list)


# print just the list elements

print(list)

# print the list in a special way
print(*list, sep=' and ', end=" --that's all folks!\n")
