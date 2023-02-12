def gen():
    yield 3
    yield 'wow'
    yield -1
    yield 1.2


# print generator values
for iterator in gen():
    print(iterator)
