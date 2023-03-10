def generatorExpression():
    result = []
    for val in (2 ** x for x in range(10)):
        result += [val]
    return result


print(generatorExpression())
