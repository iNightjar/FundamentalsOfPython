def func(**args):
    a = args['firstArguement']
    b = args['secondArguement']
    c = args['thirdArguement']

    return a + b + c


print(func(firstArguement=1, secondArguement=2, thirdArguement=3))
