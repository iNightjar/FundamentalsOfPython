def help_screen():
    """
    Displays information about how the program works.
    Accepts no parameters.
    Returns nothing.
    """
    print("Add: adds two numbers")
    print("subtract: subtract two numbers")
    print("Print: displays the result of the latest operation")
    print("Help: display this help screen")
    print("Quit: exits the program")


def menu():
    """
    diplays a menu
    accepts no parameters
    returns the string entered by the user

    """

    return input("=== A)dd  S)ubtract   P)rint  H)elp   Q)uit ==== \n")


def addTwoNumbers():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    return number1+number2


def subTwoNumbers():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    return number1-number2


def main():
    """runs a command loop that allows users to perform simple arithemtic"""
    result = 0.0
    done = False
    while not done:
        choice = menu()
        if choice == "A" or choice == 'a':
            result = addTwoNumbers()
            print(result)
        elif choice == "S" or choice == 's':
            result = subTwoNumbers()
            print(result)
        elif choice == 'P' or choice == 'p':
            print("The Result value is : ", result)
        elif choice == 'H' or choice == 'h':
            help_screen()
        elif choice == 'Q' or choice == 'q':
            print("Exit Choices")
            done = True


main()
