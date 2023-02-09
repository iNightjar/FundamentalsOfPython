def evalute(func, firstParam, secondParam):
    return func(firstParam, secondParam)


def main():
    number = int(input("enter an integer: "))
    print(evalute(lambda firstParam,
          secondParam: False if firstParam == number else True, 2, 3))


main()