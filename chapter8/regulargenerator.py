def generate_multiples(firstNumber, secondNumber):
    count = 0
    while count < secondNumber:
        yield firstNumber * count  # it's like a return
        count += 1


def main():
    for mult in generate_multiples(3, 6):
        print(mult, end=' ')
    print()


main()
