count = 1  # a global count vairable


def remember():
    global count
    count += 1
    print('callling remember (# ' + str(count) + ')')


print("Beginning program")
remember()
remember()
remember()
remember()
remember()
print("Ending program")
