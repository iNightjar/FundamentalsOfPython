def add(x, y):
    """
    adds the parameters x and y and returns the resutl
    """
    return x + y


def multiply(x, y):
    """multiplies the parameters x and y and result """

    return x * y


def evaluate(function, x, y):
    """calls the function f with paramaters x and y:
    f(x, y)"""
    return function(x, y)


def main():
    """tests the add, multiply, and evaluate functions"""
    print(add(2, 3))
    print(multiply(2, 3))
    print(evaluate(add, 2, 3))
    print(evaluate(multiply, 2, 3))


main()
