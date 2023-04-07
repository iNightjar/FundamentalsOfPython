try:
    val = int(input("Please enter a small positive integer: "))
    print("you entered", val)
    [][2] = 5  # try to assign to a nonexistent index of the empty list
except ValueError:
    print("input not accepted")
