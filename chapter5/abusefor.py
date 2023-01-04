# abuse the for statement

for i in range(10):
    print(i, end=' ')  # print i as served by the range object
    if i == 5:
        i = 20
    # output be like:  0 (0), 1 (1), 2 (2) .. etc
    print("({})".format(i), end=' ')
print()
