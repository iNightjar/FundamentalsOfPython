try:
    val = int(input("Please enter a small positive integer: "))
    print("You entered", val)
except ValueError:
    print("input not accepted")
